#The Goal: Write a script that reads portfolio.csv and prints a summary report showing how much money is invested in each unique company.
# import csv
# holdings = {}
# with open('Portfolio.csv', 'r')  as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         name = row['name']  
#         shares = int(row['shares'])
#         price = float(row['price'])
#         cost = price*shares
#         if name in holdings:
#             holdings[name] += cost
#         else:
#             holdings[name] = cost
# print(holdings)

import csv
def read_portfolio(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) ==2:
                name = row[0]
                price = float(row[1])
                prices[name] = price
    return prices
def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        name = row['name']
        shares = int(row['shares'])
        paid_price = float(row['price'])
        current_price = prices.get(name, 0.0)
        paid = shares *paid_price
        current_value = shares*current_price
        change = current_value - paid
        report.append((name,shares,paid,current_value,change))
    return report

def print_report(report):
    print(f"{'name':>10} {'shares':>10} {'paid':>10} {'current':>10} {'change':>10}")
    print('-'*60)
    for name, shares, paid, current_value, change in report:
        print(f"{name:>10} {shares:>10} {paid:>10,.2f} {current_value:>10,.2f} {change:>10,.2f}")
    print('-'*60)
    total_change = sum(change for _,_,_,_,change in report)
    print(f"{'total change':<40} {total_change:>10,.2f}")
    print('-'*60)
def portfolio_report(port_file,price_file):
    portfolio = read_portfolio(port_file)
    prices = read_prices(price_file)
    report = make_report(portfolio,prices)
    print_report(report)
if __name__ == "__main__":
    portfolio_report('Portfolio.csv', 'prices.csv')
