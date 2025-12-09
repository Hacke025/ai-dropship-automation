import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

MAX_PRODUCTS = 20

def scrape():
    url = "https://www.aliexpress.com/category/100003109/women-clothing.html"
    res = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    products = []
    for i, link in enumerate(soup.find_all("a")):
        if "item" in str(link.get("href")):
            title = link.get_text(strip=True)
            href = link.get("href")
            if title and href:
                products.append({
                    "id": f"prod_{i}",
                    "title": title,
                    "url": href
                })
        if len(products) >= MAX_PRODUCTS:
            break

    df = pd.DataFrame(products)
    df.to_csv("storefront/products.csv", index=False)
    print("✅ Scraped and saved products.csv")

if __name__ == "__main__":
    scrape()
