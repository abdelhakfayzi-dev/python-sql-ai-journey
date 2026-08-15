import csv
def read_portfolio(filename):
    with open(filename,'r') as f:
        reader = csv.DictReader(f)
        portfolio = list(reader)
    return portfolio
#print(read_portfolio('Portfolio.csv'))
def read_prices(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        d ={}
        for row in reader:
            if len(row) > 0:
                d[row[0]] = float(row[1])
    return d
#print(read_prices('prices.csv'))
# total_cost = sum(int(row['shares'])*float(row['price']) for row in read_portfolio('Portfolio.csv'))
# print(total_cost)
def build_report(portfolio, prices):
    report = []
    for row in portfolio:
        name = row['name']
        shares = int(row['shares'])
        price = float(row['price'])
        paid = price*shares
        current = shares*prices.get(name, 0.0)
        current_value = current*shares
        change = current_value - paid
        report.append({
            'name':name,
            'shares':round(shares, 2),
            'paid':round(paid, 3),
            'current':round(current, 2),
            'change':round(change, 2)
            })
    return report
portfolio = read_portfolio('Portfolio.csv')
# prices = read_prices('prices.csv')
def print_report(report):
    print(f"{'Name':>10} {'Shares':>10} {'Paid':>10} {'Current':>10} {'Change':>10}")
    print(f"{'-'*10:>10} {'-'*10:>10} {'-'*10:>10} {'-'*10:>10} {'-'*10:>10} ")
    invested = 0.0
    tcurrent = 0.0
    for row in report:
     name = row['name']
     shares = int(row['shares'])
     paid = float(row['paid'])
     current = float(row['current'])
     change = current-paid
     invested += paid
     tcurrent += current
     gainloss = tcurrent - invested

     print(f"{name:>10} {shares:>10} {paid:>10,.2f} {current:>10,.2f} {change:>10,.2f} ")
    print('-'*50)   
    print(f"Total Invested: ${invested:>40,.2f}")
    print(f"Total Current: ${tcurrent:>40,.2f}")
    print(f"Total Gain/loss: ${gainloss:>40,.2f}")
    best = None
    worst = None

    for row in report:
     change = row['change']
    
    # Track best
     if best is None or change > best['change']:
        best = row
    
    # Track worst
     if worst is None or change < worst['change']:
        worst = row
    print(f"Best: {best['name']} (${best['change']:>10,.2f})")
    print(f"Worst: {worst['name']} (${worst['change']:>10,.2f})")
def main():
    portfolio_list = read_portfolio('Portfolio.csv')
    prices = read_prices('prices.csv')
    report = build_report(portfolio_list, prices)
    print_report(report)

if __name__ == "__main__":
    main()
  