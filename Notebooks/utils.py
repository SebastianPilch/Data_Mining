import random

def generate_comment(adjectives_pos, adjectives_neg, nouns):
    """Generates random comments for food, service, and atmosphere."""
    labels = ["positive", "negative", "none"]
    comment_data = []

    for noun in nouns:
        label = random.choices(labels, weights=[0.5, 0.4, 0.1])[0]
        if label == "positive":
            adj = random.choice(adjectives_pos)
            comment = f"The {noun} was {adj}."
        elif label == "negative":
            adj = random.choice(adjectives_neg)
            comment = f"The {noun} was {adj}."
        else:
            comment = f"No opinion on the {noun}."
        comment_data.append((comment, noun, label))

    return comment_data


# Example usage
adjectives_positive = ["delicious", "excellent", "fantastic", "amazing", "wonderful"]
adjectives_negative = ["terrible", "awful", "disappointing", "bad", "horrible"]
nouns = ["food", "service", "atmosphere"]

comments = generate_comment(adjectives_positive, adjectives_negative, nouns)
for c in comments:
    print(c)
