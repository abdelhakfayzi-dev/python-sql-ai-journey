#Checks which target stocks are missing from your portfolio.
import csv
targets = ["AA", "IBM", "CAT", "MSFT", "GE", "TSLA", "GOOGL"]
actual = set()
target_set =set(targets)
with open('Portfolio.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        actual.add(row['name'])
missing = target_set - actual
print("missing stocks: ", missing)