portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]


names = [name[0] for name in portfolio]          
costs = [shares*price for name,shares,price in portfolio]          
high_price = [name for name,shares,price in portfolio if price>50]     

print(names)
print(costs)
print(high_price)