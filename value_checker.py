import csv

def read_portfolio(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        portfolio = list(reader)
    return portfolio

portfolio = read_portfolio('Portfolio.csv')
wanted = input('What stock are you interested in? ')

found = False
total_shares = 0
total_paid = 0.0

for row in portfolio:
    if row['name'] == wanted:
        shares = int(row['shares'])
        price = float(row['price'])
        
        total_shares += shares
        total_paid += price * shares
        found = True

# Print the result ONCE after checking all rows
if found:
    print(f"Total shares owned: {total_shares}")
    print(f"Total paid for all shares: ${total_paid:.2f}")
else:
    print('Stock not found')

    

