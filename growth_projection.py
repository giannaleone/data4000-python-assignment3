"""Exercise 9: Business Growth Projection"""

# Get starting values from the user
revenue = float(input("Initial revenue: $"))
growth = float(input("Annual growth rate (%): "))

# Print the table header (:<6 = left-align, :>16 = right-align)
print(f"\n{'Year':<6}{'Revenue':>16}")
print("-" * 22)

# Repeat once for each year, 1 through 10
for year in range(1, 11):
    revenue = revenue * (1 + growth / 100)  # 5% growth means multiply by 1.05
    print(f"{year:<6}${revenue:>15,.2f}")