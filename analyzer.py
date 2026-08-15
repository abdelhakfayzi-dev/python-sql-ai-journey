# Objective: Write a Python script called analyzer.py that:

# Reads portfolio.csv and prices.csv.

# Calculates gain/loss for each stock.

# Prints a formatted table showing: name, shares, paid, current, change.

# Prints a summary: total invested, total current, total gain/loss.
import csv
def read_portfolio(filename):
 with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    portfolio_list = list(reader)
 return portfolio_list 

def read_prices(filename):
  prices = {}
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      if len(row) > 0:
       prices[row[0]] = float(row[1])
  return prices

def build_report(portfolio_list, prices):
  report = []

  for row in portfolio_list:
     name = row['name']
     shares = int(row['shares'])
     price = float(row['price'])
     current = prices.get(name, 0.0)
     paid = shares*price
     current_value = current*shares
     change = current_value - paid
     d = {}
     d['name'] = name
     d['shares'] = shares
     d['paid'] = round(paid)
     d['current'] = round(current_value)
     d['change'] = round(change)
     report.append(d)
  return report
portfolio_list = read_portfolio('Portfolio.csv')
prices = read_prices('prices.csv')
# print(build_report(portfolio_list,prices))

def print_report(report):
  print(f"{'Name':>10} {'Shares':>10} {'Paid':>10} {'Current':>10} {'Change':>10} ")
  print('-'*50)
  total_paid = 0.0
  total_current = 0.0
  best = None
  worst = None
  for row in report:
    name = row['name']
    shares = int(row['shares'])
    paid = float(row['paid'])
    current = float(row['current'])
    change = float(row['change'])
    print(f"{name:>10} {shares:>10} {paid:>10,.2f} {current:>10,.2f} {change:>10,.2f} ")
    total_paid += paid
    total_current += current
    gainloss = total_current  -total_paid
    
    if best is None or change > best['change']:
     best = row
    if worst is None or change < worst['change']:
        worst = row
  print('-'*50)   
  print(f"Total Invested: ${total_paid:>40,.2f}")
  print(f"Total Current: ${total_current:>40,.2f}")
  print(f"Total Gain/loss: ${gainloss:>40,.2f}")
  print(f"Best: {best['name'] } (${best['change']:>10,.2f})")
  print(f"worst: {worst['name'] } (${worst['change']:>10,.2f})")
def main():
    portfolio_list = read_portfolio('Portfolio.csv')
    prices = read_prices('prices.csv')
    report = build_report(portfolio_list, prices)
    print_report(report)

if __name__ == "__main__":
    main()
  