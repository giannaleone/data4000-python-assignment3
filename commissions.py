"""Exercise 4: Sales Commission Calculator"""

COMMISSION_RATE = 0.10  # 10% commission

# Returns the commission for one sales amount
def calculate_commission(sales_amount, rate=COMMISSION_RATE):
    return sales_amount * rate

# Helper for sorting: pair looks like ("Alice", 500.0), so pair[1] is the commission
def get_commission(pair):
    return pair[1]

# Sales for each employee
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

# Dictionary to hold each person's commission
commissions = {}
for name, amount in sales.items():
    commissions[name] = calculate_commission(amount)  # call our function

# Sort highest commission first
ranked = sorted(commissions.items(), key=get_commission, reverse=True)

print("Commission Leaderboard")
print("----------------------")

rank = 1  # starting rank number
for name, commission in ranked:
    print(f"{rank}. {name:<6} ${commission:,.2f}")  # :<6 = left-align in 6 spaces
    rank += 1  # next person gets the next rank