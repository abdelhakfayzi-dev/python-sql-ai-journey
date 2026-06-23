#The Goal: Write a script that reads portfolio.csv and prints a formatted table
import csv
print(f'{"Company":<6} {'Shares':>8} {'Price':>8} {'Total':>12}')
print(f'{'':-<6} {'':->8} {'':->8} {'':->12}')
with open('Portfolio.csv', 'r') as f:
    reader = csv.DictReader(f)
    grand_total =0
    for row in reader:
        name = row['name']
        shares = int(row['shares'])
        price = float(row['price'])
        total = shares*price
        grand_total += total
        print(f'{name:<6} {shares:>8} {price:>8} {total:>12,.2f}')
print(f'{'':->37}') 
print(f'{'Total':<6} {grand_total:>30,.2f}')   