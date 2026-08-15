# import copy

# print("\n=== Deep Copy Example ===")
# original = [[1, 2], [3, 4]]
# shallow = original.copy()
# deep = copy.deepcopy(original)

# shallow[0][0] = 999
# deep[1][1] = 888

# print("Original:", original)  # Should have [999, 2] changed, but [3, 4] unchanged
# print("Shallow:", shallow)    # Should match original
# print("Deep:", deep)          # Should be completely untouched by shallow changes
# import copy
# original_portfolio = [
#     {"name": "IBM", "shares": 50, "price": 91.1},
#     {"name": "AAPL", "shares": 200, "price": 125.3}
# ]

# # This is the buggy part. How do we fix this?
# backup = copy.deepcopy(original_portfolio)
# # Simulate a crash (cut prices in half)
# for stock in backup:
#     stock["price"] = stock["price"] * 0.5

# print("Original:", original_portfolio)  # Should be [91.1, 125.3]
# print("Backup:", backup)                # Should be [45.55, 62.65]

import copy
def adjust(portfolio,percentage):
    deep = copy.deepcopy(portfolio)
    for stock in deep:
        stock['price'] *= percentage
        stock['price'] = round(stock['price'])
    pass
    return deep
original = [
    {"name": "GOOG", "price": 100},
    {"name": "AAPL", "price": 150},
    {"name": "MSFT", "price": 200}
]

adjusted = adjust(original,1.104)

print('original:',original)  # Unchanged
print('adjusted:',adjusted)  # All prices multiplied by 1.10