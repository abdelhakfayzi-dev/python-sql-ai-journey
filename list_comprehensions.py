# numbers = [10, 20, 30, 40, 50]
# # Create a new list with each number doubled.
# # Expected: [20, 40, 60, 80, 100]
# new = [x*2 for x in numbers]
# print(new)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Create a new list with only even numbers.
# # Expected: [2, 4, 6, 8, 10]
# new = [x for x in numbers if x%2 == 0]
# print(new)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Create a new list with squares of even numbers only.
# # Expected: [4, 16, 36, 64, 100]
# new = [x**2 for x in numbers if x%2 == 0]
# print(new)

# words = ["hello", "world", "python", "list", "comprehension"]
# # Create a new list with each word in uppercase.
# # Expected: ['HELLO', 'WORLD', 'PYTHON', 'LIST', 'COMPREHENSION']
# new = [word.upper() for word in words]
# print(new)

# words = ["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
# # Create a new list with only words that start with 'a'.
# # Expected: ['apple', 'apricot', 'avocado']
# new = [word for word in words if word[0] == 'a']
# print(new)

# portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]
# # Create a new list with only the stock names.
# # Expected: ['AA', 'IBM', 'CAT']

# new = [name[0] for name in portfolio ]
# print(new)

# portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]
# # Use a list comprehension to calculate cost per stock (shares * price).
# # Expected: [3220.0, 4555.0, 12516.0]

# cost = [shares*price for name,shares,price in portfolio]
# print(cost)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Create a new list with 'even' for even numbers, 'odd' for odd numbers.
# # Expected: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
# new = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# print(new)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Use a nested list comprehension to flatten this matrix.
# # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# flaten = [item for row in matrix for item in row]
# print(flaten)

# portfolio = [("AA", 100, 32.20), ("IBM", 50, 91.10), ("CAT", 150, 83.44)]

# # Use list comprehensions to:
# # 1. Create a list of stock names
# # 2. Create a list of total costs (shares * price)
# # 3. Calculate the total portfolio value using sum()
# # Expected output:
# # Names: ['AA', 'IBM', 'CAT']
# # Costs: [3220.0, 4555.0, 12516.0]
# # Total value: 20291.0

# names =[stock[0] for stock in portfolio]
# total_cost =[shares*price for name,shares,price in portfolio]
# total = sum(total_cost)
# print(names)
# print(total_cost)
# print(total)

import csv
with open('Portfolio.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print( row for row in rows if for name,shares,price in rows price> 50)
    