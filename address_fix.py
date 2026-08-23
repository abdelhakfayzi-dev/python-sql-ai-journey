import csv, re, time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

ADDR_RE = re.compile(r"\d{1,6}[, ]\s*[A-Za-z0-9 .#-]+?,\s?[A-Za-z .]+?,\s?(?:FL|Florida)(?:,?\s?\d{5})?")
DROP_PREFIXES = ("(631)", "(773)", "(213)")

def via_osm(name):
    try:
        r = requests.get("https://nominatim.openstreetmap.org/search",
                         params={"q": name + " Florida", "format": "json"},
                         headers={"User-Agent": "lead-enricher/1.0 (student project)"},
                         timeout=10)
        for hit in r.json():
            m = ADDR_RE.search(hit["display_name"])
            if m: return m.group(0)
    except Exception:
        pass
    return ""

def via_bing(driver, name, phone):
    try:
        driver.get(f"https://www.bing.com/search?q=%22{name}%22+{phone}")
        time.sleep(3)
        m = ADDR_RE.search(driver.find_element(By.TAG_NAME, "body").text)
        return m.group(0) if m else ""
    except Exception:
        return ""

driver = webdriver.Chrome()   # visible window = human-like, not blocked

rows = [r for r in csv.DictReader(open("florida_dumpster_rental.csv", encoding="utf-8-sig"))
        if r["Phone"] and not r["Phone"].startswith(DROP_PREFIXES)]

for row in rows:
    if row["Address"].strip() and "Serving" not in row["Address"]: continue
    addr = via_osm(row["Name"])
    if not addr:
        addr = via_bing(driver, row["Name"], row["Phone"])
        time.sleep(2)
    row["Address"] = addr or "Service area (no storefront)"
    print(f"{row['Name']} -> {row['Address']}")
    time.sleep(1.5)

driver.quit()
with open("florida_dumpster_rental_full.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["Name", "Address", "Phone"])
    w.writeheader(); w.writerows(rows)
print(f"[OK] saved {len(rows)} clean rows")