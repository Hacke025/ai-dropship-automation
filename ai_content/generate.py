import pandas as pd
from gpt4all import GPT4All
import json

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def generate():
    df = pd.read_csv("storefront/products.csv")

    generated = []
    for _, row in df.iterrows():
        prompt = f"""
        Write:
        1. A short catchy product title
        2. A 2 sentence product description

        Product: {row['title']}
        """

        output = model.generate(prompt, max_tokens=200)

        # Remove extra line breaks and placeholder text
        clean_output = output.replace("\n", " ").strip()
        generated.append({
            "id": row["id"],
            "title": row["title"].split('\n')[0],  # just take the first line as title
            "description": clean_output,
            "url": row["url"]
        })


    with open("storefront/products.json", "w") as f:
        json.dump(generated, f, indent=2)

    print("✅ AI content generated")

if __name__ == "__main__":
    generate()
