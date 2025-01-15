import random
import pandas as pd


def generate_comment(adjectives_neg, nouns):
    """Generates random negative comments for food, service, and atmosphere with varied sentence structures."""
    sentiment = "Negative"
    adj = random.choice(adjectives_neg)
    nouns_alternatives = {
        "food": ["meal", "cuisine", "dish", "menu"],
        "service": ["staff", "assistance", "hospitality", "waitstaff"],
        "atmosphere": ["ambiance", "vibe", "environment", "decor", 'atmosphere']
    }
    noun_alt = random.choice(nouns_alternatives.get(nouns, [nouns]))
    templates = [
        f"{noun_alt} bad {adj} not good experience",
        f"experience with {noun_alt} very {adj} not great",
        f"{noun_alt} too {adj} disappointed by it",
        f"expected better but {noun_alt} {adj} not satisfying",
        f"{noun_alt} really {adj} no good feelings",
        f"overall {noun_alt} {adj} would not recommend",
        f"very {adj} {noun_alt} poor quality",
        f"{noun_alt} {adj} not up to par",
        f"{noun_alt} {adj} not worth it",
        f"{noun_alt} {adj} not good enough",
        f"{noun_alt} {adj} not what expected"
    ]
    comment = random.choice(templates)
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

adjectives_negative = {
    "food": [
        "terrible", "awful", "disappointing", "bad", "horrible",
        "unpleasant", "unsatisfying", "mediocre", "dreadful", "poor",
        "overpriced", "disgusting", "unappetizing", "inedible", "bland",
        "tasteless", "soggy", "greasy", "salty", "sweet", "sour", "bitter",
        "spicy", "burnt", "raw", "undercooked", "overcooked", "stale",
        "spoiled", "rotten", "smelly"
    ],
    "service": [
        "terrible", "awful", "rude", "inattentive", "unprofessional",
        "untrained", "inexperienced", "incompetent", "disorganized",
        "slow", "unfriendly", "unhelpful", "unaccommodating", "unreliable",
        "inconsistent", "unpredictable", "unstable", "untrustworthy"
    ],
    "atmosphere": [
        "terrible", "awful", "unpleasant", "dull", "boring", "predictable",
        "unoriginal", "uninspired", "unimaginative", "uncreative",
        "uninteresting", "uneventful", "unexciting", "unimpressive",
        "unattractive", "unappealing", "uninviting", "unwelcoming",
        "uncomfortable", "outdated", "overrated", "crowded", "loud",
        "messy", "dirty"
    ]
}

# Check for Null aspects and generate negative comments if needed
for aspect in ["food", "service", "atmosphere"]:
    none_indices = df[df[aspect].isnull()].index

    # Select a random 25% of the null indices
    sample_size = max(1, int(len(none_indices) * 0.25))  # Ensure at least one is sampled if applicable
    sampled_indices = random.sample(list(none_indices), min(len(none_indices), sample_size))

    for idx in sampled_indices:
        generated_comment, sentiment = generate_comment(adjectives_negative[aspect], aspect)
        if pd.isnull(df.at[idx, "text"]):
            df.at[idx, "text"] = generated_comment
        else:
            df.at[idx, "text"] = f"{df.at[idx, 'text']} {generated_comment}".strip()
        df.at[idx, aspect] = sentiment

# Reset the index again
df.reset_index(drop=True, inplace=True)

# Save the filtered dataset
df.to_csv('../raw_data/filtered_data_.csv', index=False)
