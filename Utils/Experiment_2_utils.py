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
        if comment[0] == " ":
            comment = comment[1:]

    if comment[-1] == " ":
        comment = comment[:-1]
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
adjectives_positive = {}
adjectives_negative = {}
nouns = {}

adjectives_positive['food'] = [
    "delicious", "tasty", "fresh", "flavorful", "savory", "mouthwatering",
    "appetizing", "heavenly", "scrumptious", "exquisite", "yummy", "succulent", "delectable",
    "crunchy", "crispy", "rich", "spicy", "smooth", "balanced", "aromatic", "smooth",
    "satisfying", "warm", "homemade", "gourmet", "quality", "juicy", "nutritious",
    "creamy", "sweet", "fluffy", "zesty", "tender", "classic", "refreshing", "flaky",
    "decadent", "divine", "perfect", "healthy", "luxurious", "bold", "comforting",
    "organic", "inviting", "richly flavored", "inviting", "piping hot", "filling", "scrumptious"
]

adjectives_positive['service'] = [
    "friendly", "helpful", "attentive", "kind", "polite", "courteous", "efficient",
    "fast", "quick", "excellent", "outstanding", "exceptional", "responsive", "professional",
    "pleasant", "accommodating", "cheerful", "respectful", "knowledgeable", "warm", "personalized",
    "excellent", "top-notch", "skilled", "attentive", "smiling", "engaging", "trustworthy",
    "reliable", "approachable", "diligent", "pleasant", "considerate", "friendly", "genuine",
    "helpful", "timely", "efficient", "consistent", "gracious", "sincere", "thoughtful",
    "welcoming", "courteous", "remarkable", "enthusiastic", "engaged"
]

adjectives_positive['atmosphere'] = [
    "cozy", "welcoming", "relaxing", "inviting", "comfortable", "charming",
    "peaceful", "warm", "friendly", "pleasant", "intimate", "stylish", "elegant", "modern",
    "comfortable", "tranquil", "luxurious", "lively", "chic", "vibrant", "casual", "classy",
    "peaceful", "airy", "contemporary", "homey", "serene", "romantic", "bright", "spacious",
    "quiet", "refreshing", "enticing", "cozy", "uplifting", "modern", "fresh", "beautiful",
    "relaxing", "breezy", "chilled", "colorful", "welcoming", "inviting", "calming", "refreshing",
    "ambiance", "sophisticated", "rustic"
]

adjectives_negative['food'] = [
    "awful", "disgusting", "bland", "unappetizing", "greasy", "stale", "soggy",
    "burnt", "overcooked", "undercooked", "rotten", "spoiled", "tough", "smelly", "cold", "sour",
    "rubbery", "dry", "chewy", "bitter", "unseasoned", "salty", "inadequate", "unpleasant", "stringy",
    "gross", "lumpy", "overly greasy", "mushy", "unripe", "soggy", "flavorless", "mediocre", "slimy",
    "unhealthy", "unfresh", "unrefined", "stinky", "unflavorful", "underseasoned", "greasy",
    "spoiled", "tasteless", "too salty", "over-sweetened", "disappointing", "gummy"
]

adjectives_negative['service'] = [
    "rude", "slow", "unprofessional", "unhelpful", "disorganized", "inattentive",
    "impolite", "disrespectful", "awkward", "unfriendly", "arrogant", "incompetent", "inefficient",
    "unresponsive", "unaccommodating", "unpleasant", "unreliable", "untrustworthy", "irritating",
    "disengaged", "disinterested", "poor", "overwhelmed", "unpleasant", "dismissive", "overworked",
    "disrespectful", "distracting", "clumsy", "overbearing", "nonchalant", "unskilled", "insincere",
    "impolite", "careless", "unconsiderate", "hasty", "inadequate", "unpleasant", "annoying",
    "unaware", "unhelpful", "hostile", "awkward", "confused", "cold"
]

adjectives_negative['atmosphere'] = [
   "uncomfortable", "noisy", "dark", "disagreeable", "stuffy", "cold", "unwelcoming",
    "chaotic", "cluttered", "depressing", "uninviting", "awkward", "sterile", "unpleasant", "boring",
    "unpleasant", "overcrowded", "unromantic", "shabby", "gloomy", "isolated", "cold", "soulless",
    "disorienting", "oppressive", "too bright", "unfriendly", "harsh", "dirty", "uncomfortable",
    "too loud", "unappealing", "stale", "unrelaxed", "uninspiring", "stressful", "unpleasant",
    "unwelcoming", "unbalanced", "uncomfortable", "bland", "unsightly", "harsh lighting", "unsophisticated",
    "unpolished", "dull", "noisy", "chaotic"
]

nouns['food'] = [
    "pizza", "burger", "sushi", "pasta", "sandwich", "salad", "steak",
    "soup", "tacos", "curry", "noodles", "chicken", "fish", "potatoes",
    "dessert", "cake", "cookies", "pancakes", "waffles", "ice cream",
    "cheese", "fruit", "vegetables", "rice", "bread", "soup", "pie",
    "chocolate", "spaghetti", "lasagna", "smoothie", "coffee", "tea",
    "hamburger", "chips", "sausages", "gravy", "fried rice", "casserole",
    "quiche", "wrap", "muffin", "sushi rolls", "fish and chips", "tofu",
    "quinoa", "paella", "guacamole", "pasta salad", "dish", "meal",
    "course", "snack", "appetizer", "entrée", "side dish", "main course",
    "beverage", "drink", "juice", "soft drink", "cocktail", "platter",
    "buffet", "brunch", "breakfast", "lunch", "dinner", "feast", "banquet",
    "picnic", "spread", "delicacy", "treat", "entree", "concoction"
]

nouns['service'] = [
    "waiter", "waitress", "host", "hostess", "receptionist", "attendant",
    "delivery", "concierge", "customer service", "chef", "busboy", "bartender",
    "manager", "assistant", "guide", "technician", "cleaner", "caretaker",
    "valet", "reservation", "check-in", "room service", "waitstaff", "dishwasher",
    "service desk", "security", "support", "team", "staff", "delivery person",
    "clerk", "helper", "customer support", "help desk", "concierge", "bellboy",
    "waitperson", "server", "attendant", "order taker", "account manager",
    "service representative", "team member", "caregiver", "maintenance", "housekeeper",
    "online ordering", "phone ordering", "delivery service", "pickup service",
    "order confirmation", "support agent", "live chat", "chatbot", "e-commerce",
    "order tracking", "call center", "support hotline", "customer care",
    "virtual assistant", "order processing", "customer inquiry", "remote service",
    "automated service", "online support", "telephonic service", "digital assistant"
]

nouns['atmosphere'] = [
    "ambiance", "lighting", "decor", "room", "space", "environment",
    "vibe", "mood", "interior", "space", "setting", "surroundings", "feel", "tone", "background",
    "energy", "air", "atmosphere", "warmth", "charm", "style", "comfort", "coziness", "hospitality",
    "layout", "furnishing", "structure", "feelings", "vibration", "indoor", "outdoor", "music", "sound",
    "view", "art", "furniture", "acoustics", "charm", "aura", "temperature", "space", "ambience",
    "setting", "design", "outlook", "sight", "visuals", "mood"
]

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
            if counts[1] > counts[2] and counts[1] > counts[0]:
                sentiment[category] = "Positive"
                missing_comments[category][1] -= 1
            elif counts[2] > counts[0]:
                sentiment[category] = "Negative"
                missing_comments[category][2] -= 1
            else:
                sentiment[category] = None
                missing_comments[category][0] -= 1

    if all(value is None for value in sentiment.values()):
        category_to_update = random.choice(['food', 'service', 'atmosphere'])
        Pos_neg = random.choice(["Positive", "Negative"])
        sentiment[category_to_update] = Pos_neg
        if Pos_neg == "Positive":
            missing_comments[category_to_update][0] += 1
            missing_comments[category_to_update][2] += 1
        if Pos_neg == "Negative":
            missing_comments[category_to_update][0] += 1
            missing_comments[category_to_update][1] += 1


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


