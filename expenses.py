"""Exercise 3: Expense Report Categorizer"""

# Each category has a list of expense amounts
expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100],
}

grand_total = 0  # running total across ALL categories

print("=" * 34)  # "=" repeated 34 times makes a line
print("       EXPENSE SUMMARY REPORT")
print("=" * 34)

# Outer loop: one pass per category
for category, amounts in expenses.items():
    category_total = 0  # reset to 0 for each new category
    print(f"\n{category}:")

    # Inner loop: one pass per expense in this category
    for amount in amounts:
        print(f"   ${amount:>8,.2f}")  # :>8 = right-align in 8 spaces
        category_total += amount       # add to this category's total

    print(f"   {'-' * 9}")
    print(f"   Subtotal: ${category_total:,.2f}")
    grand_total += category_total      # add the subtotal to the grand total

print("\n" + "=" * 34)
print(f"GRAND TOTAL: ${grand_total:,.2f}")
print("=" * 34)