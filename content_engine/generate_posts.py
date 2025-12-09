import json

INPUT_FILE = "storefront/products.json"
OUTPUT_FILE = "content_engine/posts.json"

def generate():
    with open(INPUT_FILE, "r") as f:
        products = json.load(f)

    posts = []

    for p in products:
        post = {
            "title": f"People can't stop buying this: {p.get('title', 'Unknown Product')}",
            "hook": "You won’t believe what this can do...",
            "caption": f"{p.get('description', 'Check this out!')} #budgetfinds #coolproducts",
            "link": p.get("link", "#")
        }
        posts.append(post)


    with open(OUTPUT_FILE, "w") as f:
        json.dump(posts, f, indent=2)

    print("✅ Social content generated!")

generate()
