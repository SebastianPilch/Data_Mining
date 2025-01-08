import random
import pandas as pd


def generate_comment(adjectives_pos, adjectives_neg, nouns, sentiment):
    """Generates random comments for food, service, and atmosphere."""
    comment = ""
    for aspect in ["food", "service", "atmosphere"]:
        if sentiment[aspect] == "Positive":
            comment += random.choice(adjectives_pos[aspect]) + " " + random.choice(nouns[aspect])
        if sentiment[aspect] == "Negative":
            comment += random.choice(adjectives_neg[aspect]) + " " + random.choice(nouns[aspect])
        comment += " "
    return comment


# Load and filter dataset
df = pd.read_csv('../raw_data/clean_data.csv')  # Load your dataset

df_low_score = df[df['rating'] < 5]

# Sample 300 reviews with a score of 5
df_score_5_sample = df[df['rating'] == 5].sample(n=500, random_state=42)

# Combine the two DataFrames
df_filtered = pd.concat([df_low_score, df_score_5_sample])

# Reset the index if needed
df_filtered.reset_index(drop=True, inplace=True)

# df = df_filtered

# Balance the dataset by generating synthetic comments if needed
adjectives_positive = {
    "food":
        [
            "good",
            "nice"
        ],
    "service":
        [
            "good",
            "nice"
        ],
    "atmosphere":
        [
            "good",
            "nice"
        ]
}
adjectives_negative = {
    "food":
        [
            "bad",
            "terrible"
        ],
    "service":
        [
            "bad",
            "terrible"
        ],
    "atmosphere":
        [
            "bad",
            "terrible"
        ]
}
nouns = {
    "food":
        [
            "food1",
            "food2"
        ],
    "service":
        [
            "service1",
            "service2"
        ],
    "atmosphere":
        [
            "atmosphere1",
            "atmosphere2"
        ]
}

# df_ratings_values = df_filtered[["food", "service", "atmosphere"]]
df_ratings_values = df[["food", "service", "atmosphere"]]

none_count = df_ratings_values.isna().sum().tolist()
positive_count = (df_ratings_values == 'Positive').sum().tolist()
negative_count = (df_ratings_values == 'Negative').sum().tolist()

food_ratings_number = [none_count[0], positive_count[0], negative_count[0]]
service_ratings_number = [none_count[1], positive_count[1], negative_count[1]]
atmosphere_ratings_number = [none_count[2], positive_count[2], negative_count[2]]

missed_food_comments = [max(food_ratings_number) - i for i in food_ratings_number]
missed_service_comments = [max(service_ratings_number) - i for i in service_ratings_number]
missed_atmosphere_comments = [max(atmosphere_ratings_number) - i for i in atmosphere_ratings_number]

print(food_ratings_number)
print(service_ratings_number)
print(atmosphere_ratings_number)

print(missed_food_comments)
print(missed_service_comments)
print(missed_atmosphere_comments)

missing_comments = {
    'food': missed_food_comments,
    'service': missed_service_comments,
    'atmosphere': missed_atmosphere_comments
}

added_comments = 0

df_generated = pd.DataFrame(columns=df.columns)
print(df.columns.values)
# Generowanie komentarzy do osiągnięcia samych zer
while any(count > 0 for counts in missing_comments.values() for count in counts):
    sentiment = {}

    for category, counts in missing_comments.items():
        if counts[0] == 0 and counts[1] == 0 and counts[2] == 0:
            sentiment[category] = None
            missing_comments[category][1] += 1
            missing_comments[category][2] += 1

        else:
            if counts[1] > counts[2] and counts[1] > counts[0]:  # Więcej brakujących komentarzy pozytywnych
                sentiment[category] = "Positive"
                missing_comments[category][1] -= 1
            elif counts[2] > counts[0]:  # Więcej brakujących komentarzy negatywnych
                sentiment[category] = "Negative"
                missing_comments[category][2] -= 1
            else:
                sentiment[category] = None
                missing_comments[category][0] -= 1

    comment = generate_comment(adjectives_positive, adjectives_negative, nouns, sentiment)
    added_comments += 1

    new_entry = {col: None for col in df.columns}
    new_entry["food"] = sentiment["food"]
    new_entry["service"] = sentiment["service"]
    new_entry["atmosphere"] = sentiment["atmosphere"]
    new_entry["text"] = comment
    df_generated = pd.concat([df_generated, pd.DataFrame([new_entry])], ignore_index=True)


print(len(df))
print(added_comments)
# df.reset_index(drop=True, inplace=True)
#
# df.to_csv('../raw_data/filtered_data.csv', index=False)


df_generated.to_csv('../raw_data/generated_data.csv', index=False)
