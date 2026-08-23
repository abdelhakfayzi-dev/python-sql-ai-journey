import csv, re, time, random
import requests
from bs4 import BeautifulSoup

EMAIL_RE = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
FREE = ["gmail.com","yahoo.com","hotmail.com","aol.com","outlook.com","example.com","w3.org","schema.org"]
DIRS = ["yellowpages","yelp","facebook","bbb.org","manta","superpages","angieslist"]

def find_domain(name, city):
    r = requests.get("https://html.duckduckgo.com/html/", params={"q": f'"{name}" {city}'},
                     headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.select("a.result__a"):
        m = re.search(r'uddg=([^&]+)', a.get("href", ""))
        url = m.group(1) if m else a.get("href", "")
        m2 = re.search(r'https?://([^/]+)', url)
        if m2:
            dom = m2.group(1).lower()
            if not any(x in dom for x in FREE + DIRS):
                return dom
    return None

def scrape_email(domain):
    for path in ["", "/contact", "/contact-us"]:
        try:
            r = requests.get(f"https://{domain}{path}", timeout=8,
                             headers={"User-Agent": "Mozilla/5.0"})
            emails = [e for e in EMAIL_RE.findall(r.text)
                      if e.split("@")[1].lower() not in FREE]
            same = [e for e in emails if e.split("@")[1].lower() in domain]
            if same: return same[0]
            if emails: return emails[0]
        except Exception:
            continue
    return f"info@{domain}"

rows = list(csv.DictReader(open("servgrow_sample.csv", encoding="utf-8-sig")))
for row in rows:
    dom = find_domain(row["Name"], row["Address"])
    row["Email"] = scrape_email(dom) if dom else ""
    print(row["Name"], "->", row["Email"])
    time.sleep(random.uniform(2, 4))

with open("servgrow_sample_emails.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["Name","Address","Phone","Fit","Email"])
    w.writeheader(); w.writerows(rows)
print("[OK] saved servgrow_sample_emails.csv")
