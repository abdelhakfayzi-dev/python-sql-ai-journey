# 1. Basic f-string
name = "AA"
price = 32.20
print(f"Stock: {name}, Price: ${price:.2f}")

# 2. Formatting with alignment
company = "IBM"
print(f"{company:>10}")   # Right-align 10 chars
print(f"{company:<10}")   # Left-align 10 chars
print(f"{company:^10}")   # Center-align 10 chars

# 3. Percentage
pass_rate = 0.853
print(f"Pass rate: {pass_rate:.1%}")   # 85.3%

# 4. Thousands separator
big_number = 1234567.89
print(f"Large number: {big_number:,.2f}")

# 5. Combining specifiers
price = 1234.567
print(f"Price: ${price:>10,.2f}")   # Right-align with commas and 2 decimals