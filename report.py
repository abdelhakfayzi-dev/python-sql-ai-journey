import csv

with open('portfolio.csv', 'r') as f:
    reader = csv.DictReader(f)
    portfolio = list(reader)

total = 0.0
for row in portfolio:
    total += int(row['shares']) * float(row['price'])

print(f"Total: ${total:,.2f}")

def read_portfolio(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
def calculate_total(portfolio):
    total = 0
    for row in portfolio:
        total += int(row['shares'])*float(row['price'])
    return total
def print_report(portfolio):
    total = calculate_total(portfolio)
    print(f'Total is : {total:,.2f}')
def main():
    portfolio = read_portfolio('Portfolio.csv')
    print_report(portfolio)

if __name__ =='__main__':
    main()