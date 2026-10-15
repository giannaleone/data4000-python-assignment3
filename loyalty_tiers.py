"""Exercise 8: Customer Loyalty Tiers"""

# Returns the tier name based on how much the customer spent
def get_tier(amount):
    if amount >= 5000:      # check the highest tier first
        return "Gold"
    elif amount >= 1000:    # 1000 to 4999.99
        return "Silver"
    else:                   # under 1000
        return "Bronze"

# Each customer's total purchase amount
customers = {
    "Alice": 450,
    "Bob": 1200,
    "Carol": 5300,
    "Dan": 999.99,
    "Eve": 4999,
    "Frank": 7500,
    "Grace": 1000,
}

# Counter for each tier, all starting at 0
tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}

# Assign a tier to every customer
for name, amount in customers.items():
    tier = get_tier(amount)   # find their tier
    tier_counts[tier] += 1    # add 1 to that tier's count
    print(f"{name:<6} ${amount:>9,.2f} -> {tier}")

# Print how many customers are in each tier
print("\nTier Summary")
print("------------")
for tier, count in tier_counts.items():
    print(f"{tier}: {count} customer(s)")