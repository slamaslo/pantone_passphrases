import json
import random
from collections import Counter, defaultdict

# random.seed(0)

# 1. READ JSON
def load_categories(filename="pantone_semantic_categories.json"):
    with open(filename, "r") as f:
        categories = json.load(f)
    return categories

# 2. PASSWORD GENERATOR
def weighted_random_category(categories):
    cats = list(categories.keys())
    weights = [len(categories[c]) for c in cats]   # proportional to category size
    return random.choices(cats, weights=weights, k=1)[0]

def make_password(categories, number_range=(100, 999)):
    # pick 2 distinct categories
    cat1 = weighted_random_category(categories)
    cat2 = weighted_random_category(categories)

    # enforce distinct categories
    while cat2 == cat1:
        cat2 = weighted_random_category(categories)

    # pick 1 random color from each category
    color1 = random.choice(categories[cat1])
    color2 = random.choice(categories[cat2])

    # clean formatting
    color1 = color1.replace(" ", "-")
    color2 = color2.replace(" ", "-")

    # number
    number = random.randint(*number_range)

    return f"{color1}-{color2}-{number}"

# 3. MAIN
if __name__ == "__main__":
    categories = load_categories()
    
    print("\nExamples:")
    for _ in range(25):
        print(make_password(categories))