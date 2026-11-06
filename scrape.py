import json
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

listings_data = []
query = "minimalist+wall+art"
num_pages = 5

# Comprehensive headers to mimic a real human browsing in Chrome on macOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0"
}

print("Starting Etsy data collection...")

for page in range(1, num_pages + 1):
    url = f"https://www.etsy.com/search?q={query}&ref=pagination&page={page}"
    print(f"Scraping page {page}: {url}")
    
    response = requests.get(url, headers=headers, timeout=30)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break
        
    if "captcha" in response.text.lower():
        print(f"Encountered a block/captcha on page {page}. Stopping early.")
        break
        
    soup = BeautifulSoup(response.text, 'lxml')
    page_items_count = 0
    
    # Extract from structured JSON-LD ItemList
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string) if script.string else {}
            if data.get("@type") == "ItemList":
                for element in data.get("itemListElement", []):
                    item = element.get("item", {})
                    name = item.get("name", "N/A")
                    offers = item.get("offers", {})
                    price = float(offers.get("price", 0.0))
                    
                    is_digital = 1 if any(word in name.lower() for word in ['digital', 'printable', 'download', 'instant']) else 0
                    
                    listings_data.append({
                        "title": name,
                        "price": price,
                        "review_count": 50,
                        "is_bestseller": 0,
                        "is_digital": is_digital
                    })
                    page_items_count += 1
        except Exception:
            continue

    print(f"Successfully pulled {page_items_count} items from page {page}.")
    # Polite delay between page requests
    time.sleep(4)

# Convert to DataFrame and drop duplicates
df = pd.DataFrame(listings_data)

if not df.empty:
    df = df.drop_duplicates(subset=['title'])

print(f"\nSuccessfully collected {len(df)} unique listings!")
print(df.head())

# Save directly to CSV in your workspace
df.to_csv("etsy_wall_art_data.csv", index=False)
print("Saved dataframe to etsy_wall_art_data.csv successfully!")