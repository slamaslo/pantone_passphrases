import json
from collections import Counter, defaultdict

# 1. READ JSON
def load_pantone(filename="pantone-colors.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["names"]

# 2. BUILD SEMANTIC CATEGORIES
def tokenize(name: str):
    return name.replace("-", " ").split()


def build_categories(names, top_n=10):
    token_counts = Counter()

    # count all token frequencies
    for name in names:
        for tok in tokenize(name):
            token_counts[tok] += 1

    # get the most common tokens as category keys
    most_common_tokens = [tok for tok, _ in token_counts.most_common(top_n)]

    categories = defaultdict(list)

    # assign each name to all categories it matches
    for name in names:
        for tok in most_common_tokens:
            if tok in name:
                categories[tok].append(name)

    return categories

# 3. SAVE CATEGORIES TO JSON
def save_categories(categories, filename="../generator/pantone_semantic_categories.json"):
    with open(filename, "w") as f:
        json.dump(categories, f, indent=2)

# 4. MAIN
if __name__ == "__main__":
    names = load_pantone()

    # build semantic categories automatically
    categories = build_categories(names, top_n=30)

    # save to JSON (one time)
    save_categories(categories)

    # # show available categories (top tokens)
    # print("Available categories (top tokens):")
    # print(list(categories.keys()))

    # # print category sizes
    # for cat, items in categories.items():
    #     print(cat, len(items))
