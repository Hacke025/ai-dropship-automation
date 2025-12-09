import pandas as pd
from gpt4all import GPT4All
import json
import re

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def clean_text(text):
    # Remove numbered lists and placeholders
    text = re.sub(r"\d+\.", "", text)
    text = text.replace("Product:", "").strip()
    # Remove extra spaces
    text = " ".join(text.split())
    return text

def generate():
    df = pd.read_csv("storefront/products.csv")

    products = []
    for _, row in df.iterrows():
        prompt = f"""
Create a SHORT clean product listing:
Title: max 6 words
Description: max 2 short sentences

Product: {row['title']}
"""

        output = model.generate(prompt, max_tokens=120)
        clean = clean_text(output)

        # Split into title + description if possible
        lines = clean.split(".")
        title = lines[0][:60]
        description = ". ".join(lines[1:3]).strip()

        products.append({
            "id": row["id"],
            "title": title,
            "description": description,
            "url": row["url"]
        })

    with open("storefront/products.json", "w") as f:
        json.dump(products, f, indent=2)

    print("✅ Clean AI products generated")

if __name__ == "__main__":
    generate()
