"""Exercise 10: Startup Pitch Deck Visualizer (ASCII Style)"""

# Projected revenue in $ thousands for each year
revenue = {1: 30, 2: 50, 3: 80, 4: 120, 5: 170}

SCALE = 10  # each "#" stands for $10K

print("Projected Revenue by Year (each # = $10K)")
print("-" * 42)

# Version 1: string multiplication
for year, amount in revenue.items():
    bars = "#" * (amount // SCALE)   # "#" * 3 gives "###"
    print(f"Year {year}: {bars} (${amount}K)")

# Version 2: nested loop builds the bar one "#" at a time
print("\nNested-loop version:")
for year, amount in revenue.items():
    line = ""                          # start with an empty bar
    for _ in range(amount // SCALE):   # repeat once per "#" needed
        line += "#"                    # add one "#"
    print(f"Year {year}: {line}")