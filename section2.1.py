#TUPLES

#list = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
#print(list)
#list.insert(2,'META')
#print(list)
#list.remove('TSLA')
#print(list)

#DICTIONARIES
# example = {
#     'name': 'GOOG',
#     'shares': 100,
#     'price': 490.1
# }
# print(example['name'], example['price'])
# # add or modify values:
# example['name'] = 'META'
# example['date'] = '22/06/2026'
# print(example['name'], example['date'])
# # to delete a value we use del statement
# del example['date']
# print(example)

#Exercise 2.1: Tuples
import csv
f = open('Portfolio.csv', 'r')
rows = csv.reader(f)
next(rows)
row = next(rows)
t = (row[0], int(row[1]), float(row[2]))
cost = t[1]*t[2]
name , shares, price = t
t = (name, shares, price)
# print(t) #('AA', 100, 32.2)
# print(f'{cost:.2f}')

#Exercise 2.2: Dictionaries as a data structure
# d = {
#   'name': row[0],
#   'shares': int(row[1]),
#   'price': float(row[2]),
#  }
# print(d) #{'name': 'AA', 'shares': '100', 'price': '32.20'}
# cost = d['shares']*d['price']
# print(cost)

#keys and items 
import csv

with open('portfolio.csv', 'r') as f:
    reader = csv.DictReader(f)
    row = next(reader)  # First data row

print(row.keys())   # dict_keys(['name', 'shares', 'price'])
print(row.items())  # dict_items([('name', 'AA'), ('shares', '100'), ('price', '32.20')])

# Access by key
print(row['name'])  # 'AA'