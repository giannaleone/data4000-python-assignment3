"""Exercise 5: Stock Portfolio Tracker (with bonus simulation)"""
import random  # lets us generate random numbers

# Each stock has a number of shares and a price per share
portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130},
}

# Adds up shares * price for every stock
def total_value(pf):
    total = 0
    for info in pf.values():                  # info is the inner dictionary
        total += info["shares"] * info["price"]
    return total

print("Starting Portfolio")
for ticker, info in portfolio.items():
    print(f"  {ticker}: {info['shares']} shares @ ${info['price']:.2f} "
          f"= ${info['shares'] * info['price']:,.2f}")
print(f"Total value: ${total_value(portfolio):,.2f}")

# Bonus: simulate 7 days of price changes
print("\nOne-Week Simulation")
for day in range(1, 8):                       # outer loop: days 1 to 7
    for info in portfolio.values():           # inner loop: each stock
        change = random.uniform(-0.05, 0.05)  # random number from -5% to +5%
        info["price"] *= (1 + change)         # apply the change to the price
    print(f"Day {day}: ${total_value(portfolio):,.2f}")