import csv
def portfolio_cost(filename):
    total = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total += nshares*price
    return total
portfolio_cost('Portfolio.csv')
print(portfolio_cost('Portfolio.csv'))