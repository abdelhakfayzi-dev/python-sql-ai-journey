stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
# 1. Print the length of the list
# 2. Print the last element using negative indexing
# 3. Print the first two elements using slicing
# 4. Add "META" to the end
# 5. Insert "NVDA" at index 2
# 6. Remove "TSLA"
# 7. Sort the list alphabetically
# 8. Reverse the list
# 9. Print the final list

# #1
# print(len(stocks))
# #2
# print(stocks[-1])
# #3
# print(stocks[:2])
# #4
# stocks.append('META')
# #5
# stocks.insert(2, 'NVDA')
# #6
# stocks.remove('TSLA')
# #7 
# stocks.sort()
# #8
# stocks.reverse()
# #9
# print(stocks)

# Given this list of tuples (each tuple = name, shares, price)
# portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]

# # Write a loop that unpacks each tuple into name, shares, price
# # and prints: "Company: AA, Shares: 100, Price: 32.20"
# for name, shares, price in portfolio:
#     print(f'company: {name}, shares: {shares}, price: {price}')

# portfolio_stocks = {"AA", "IBM", "CAT", "MSFT", "GE"}
# target_stocks = {"AA", "IBM", "CAT", "MSFT", "GE", "TSLA", "GOOGL"}

# # 1. Add "NVDA" to portfolio_stocks
# # 2. Try adding "AA" again (what happens?)
# # 3. Find the intersection (stocks in both sets)
# # 4. Find the difference (stocks in target but not in portfolio)
# # 5. Find the union (all stocks)
# #1
# portfolio_stocks.add('NVDA')
# #2
# portfolio_stocks.add('AA')
# #nothing happened cuz "AA" already exists in the set
# #3
# print(portfolio_stocks & target_stocks)
# #4
# print( target_stocks - portfolio_stocks )
# #5
# print(portfolio_stocks | target_stocks)

# holdings = {"AA": 3220.0, "IBM": 11599.0, "CAT": 12516.0, "MSFT": 13501.0, "GE": 3835.15}

# # 1. Print the value for "IBM"
# # 2. Add "NVDA" with value 5000.0
# # 3. Update "GE" to 4000.0
# # 4. Remove "CAT"
# # 5. Print all keys
# # 6. Print all values
# # 7. Print all items (key-value pairs)
# # 8. Loop through the dictionary and print each key and value

# #1
# print(holdings["IBM"])
# #2
# holdings["NVDA"] = 5000.0
# #3
# holdings["GE"] = 4000.0
# #4
# del holdings["CAT"]
# #5
# for key in holdings:
#     print(key)
# #6
# print("values: ", holdings.values())
# #7
# print(holdings.items())
# #8
# for key, value in holdings.items():
#     print(f'{key}: {value}')

portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]

# Convert this list of tuples into a dictionary where:
# - The key is the company name
# - The value is the total cost (shares * price)
# Expected output: {"AA": 3220.0, "IBM": 4555.0, "CAT": 12516.0}

d = {}
for name, shares, price in portfolio:
    d[name] = round((int(shares) * float(price)))
print(d)
