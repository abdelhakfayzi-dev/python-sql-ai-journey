total_cost = sum(int(row['shares'])*float(row['price']) for row in read_portfolio('Portfolio.csv'))
# print(total_cost)