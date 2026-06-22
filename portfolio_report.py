#The Goal: Write a script that reads portfolio.csv and prints a summary report showing how much money is invested in each unique company.
import csv
holdings = {}
with open('Portfolio.csv', 'r')  as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['name']  
        shares = int(row['shares'])
        price = float(row['price'])
        cost = price*shares
        if name in holdings:
            holdings[name] += cost
        else:
            holdings[name] = cost
print(holdings)

