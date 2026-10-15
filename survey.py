"""Exercise 2: Market Survey Analyzer"""

# Fake survey data: what each customer picked
responses = ["coffee", "tea", "coffee", "soda", "coffee", "tea", "soda", "coffee"]

# Dictionary to count votes, like {"coffee": 4, "tea": 2}
counts = {}

# Go through each answer one by one
for choice in responses:
    if choice in counts:
        counts[choice] += 1   # already seen it, so add 1
    else:
        counts[choice] = 1    # first time seeing it, so start at 1

total = len(responses)  # total number of people surveyed

print("Market Share Summary")
print("--------------------")

# Go through each product and its vote count
for product, n in counts.items():
    share = n / total * 100          # convert the count to a percentage
    print(f"{product}: {share:.0f}%")  # :.0f = no decimals