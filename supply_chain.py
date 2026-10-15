"""Exercise 7: Simple Supply Chain Tracker"""

# List of warehouses; each one is a dictionary with a name and inventory
warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
]

# Will hold the combined stock, like {"apples": 300}
totals = {}

# Outer loop: each warehouse
for warehouse in warehouses:
    # Inner loop: each product in that warehouse's inventory
    for product, qty in warehouse["inventory"].items():
        if product in totals:
            totals[product] += qty   # product already counted, so add more
        else:
            totals[product] = qty    # first time seeing this product

print("Total Stock Across Supply Chain")
print("-------------------------------")
for product, qty in totals.items():
    print(f"{product.title()}: {qty}")  # title() capitalizes the first letter