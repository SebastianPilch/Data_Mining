import random
import pandas as pd


def generate_comment(adjectives_pos, adjectives_neg, nouns):
    """Generates random comments for food, service, and atmosphere."""
    sentiment = random.choices(["Negative", "Positive"], weights=[0.8, 0.2])[0]
    if sentiment == "Positive":
        adj = random.choice(adjectives_pos)
        comment = f"The {nouns} was {adj}."
    else:
        adj = random.choice(adjectives_neg)
        comment = f"The {nouns} was {adj}."
    return comment, sentiment


# Load and filter dataset
df = pd.read_csv('../raw_data/clean_data.csv')  # Load your dataset

df_low_score = df[df['rating'] < 5]

# Sample 300 reviews with a score of 5
df_score_5_sample = df[df['rating'] == 5].sample(n=500, random_state=42)

# Combine the two DataFrames
df_filtered = pd.concat([df_low_score, df_score_5_sample])

# Reset the index if needed
df_filtered.reset_index(drop=True, inplace=True)

df = df_filtered

# Balance the dataset by generating synthetic comments if needed
adjectives_positive = ["delicious", "excellent", "fantastic", "amazing", "wonderful"]
adjectives_negative = ["terrible", "awful", "disappointing", "bad", "horrible"]

# Check for Null aspects and generate negative comments if needed
for aspect in ["food", "service", "atmosphere"]:
    none_indices = df[df[aspect].isnull()].index

    for idx in none_indices:
        generated_comment, sentiment = generate_comment(adjectives_positive, adjectives_negative, aspect)
        df.at[idx, "text"] = f"{df.at[idx, 'text']} {generated_comment}".strip()
        df.at[idx, aspect] = sentiment

# Reset the index again
df.reset_index(drop=True, inplace=True)

# Save the filtered dataset
df.to_csv('../raw_data/filtered_data.csv', index=False)