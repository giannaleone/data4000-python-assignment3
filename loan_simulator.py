"""Exercise 6: Bank Loan Repayment Simulator"""

# Simulates paying off a loan month by month
def simulate_loan(balance, annual_rate, payment):
    monthly_rate = annual_rate / 100 / 12  # convert yearly % to monthly decimal
    months = 0
    total_interest = 0

    # Keep going until nothing is owed
    while balance > 0:
        interest = balance * monthly_rate   # interest charged this month
        balance = balance + interest        # add interest to what is owed
        total_interest += interest          # track total interest paid

        if payment >= balance:  # last payment may be smaller than usual
            balance = 0         # loan is fully paid
        else:
            balance -= payment  # normal monthly payment

        months += 1  # one more month passed
    return months, total_interest

# Get inputs from the user
loan = float(input("Loan amount: $"))
rate = float(input("Annual interest rate (%): "))
payment = float(input("Monthly payment: $"))

# Interest for the first month
first_month_interest = loan * rate / 100 / 12

# If payment can't beat the interest, the loop would never end
if payment <= first_month_interest:
    print("Your payment doesn't cover the monthly interest, "
          "so the loan can never be paid off.")
else:
    months, interest = simulate_loan(loan, rate, payment)
    years = months // 12  # // = whole-number division
    rem = months % 12     # % = remainder
    print(f"\nThe loan will be paid off in {months} months ({years} years, {rem} months).")
    print(f"Total interest paid: ${interest:,.2f}")