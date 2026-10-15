"""Exercise 1: Retail Checkout Simulation"""
 
# Checks if the text is a valid non-negative number like 4 or 4.99
def is_valid_price(text):
    # Remove one decimal point, then check that only digits are left
    return text.replace(".", "", 1).isdigit()
 
# Empty list to store every price entered
prices = []
 
# Keep asking until the user types 0
while True:
    entry = input("Enter item price (0 to finish): $").strip()  # strip() removes extra spaces
 
    # If the input isn't a valid number, warn and ask again
    if not is_valid_price(entry):
        print("Please enter a valid, non-negative number.")
        continue  # jump back to the top of the loop
 
    price = float(entry)  # convert text to a number
 
    # 0 means the customer is done, so leave the loop
    if price == 0:
        break
 
    prices.append(price)  # add the price to the list
 
# Number of items = length of the list
count = len(prices)
 
# Avoid dividing by zero if nothing was bought
if count == 0:
    print("No items were purchased.")
else:
    total = sum(prices)  # add up all prices
    print("\n--- Receipt Summary ---")
    print(f"Number of items: {count}")
    print(f"Total purchase:  ${total:,.2f}")            # :,.2f = commas + 2 decimals
    print(f"Average item:    ${total / count:,.2f}")    # average = total / count