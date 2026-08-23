import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

print("=" * 40)
print("PRICE TRACKER")
print("=" * 40)

try:
    with sqlite3.connect("prices.db") as conn:
        cursor = conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS prices(
        url TEXT,
        name TEXT,
        price REAL,
        timestamp TEXT)''')
        for url in urls:
            
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("h1").get_text(strip=True)
            price = float(soup.find("span", class_="price_amount").get_text(strip=True).replace('MAD','').replace(',', '.').strip())
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("SELECT price FROM prices WHERE url=? ORDER BY timestamp DESC LIMIT 1", (url,))
            row = cursor.fetchone()
            prev_price = row[0] if row else None
            cursor.execute("INSERT INTO prices VALUES (?,?,?,?)", (url, title, price, now))
            conn.commit()
            if prev_price is None:
                print(f"[NEW] {title} at {price}")
            elif price < prev_price:
                print(f"[DROP] {title} dropped from {prev_price} to {price}")
            elif price > prev_price:
                print(f"[RISE] {title} rose from {prev_price} to {price}")
            else:
             print(f"[SAME] {title} unchanged at {price}")
    pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)
print("=" * 40)
print(f"Tracked: {len(urls)} products")







# 3. For each URL:
#    - fetch the page
#    - parse the title
#    - parse the price (look for € symbol)
#    - get previous price from DB
#    - insert new price
#    - compare: new vs old → print DROP / RISE / SAME / NEW

# 4. Print clean report