investment_amount = float(input("Enter the investment amount: "))
monthly_payment = float(input("Enter the monthly payment: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
num_years = int(input("Enter the number of years: "))

FV = investment_amount * ((1 + annual_interest_rate / 12 / 100) ** (num_years * 12)) + monthly_payment * ((((1 + annual_interest_rate / 12 / 100) ** (num_years * 12)) - 1) / (annual_interest_rate / 12 / 100)) * (1 + annual_interest_rate / 12 / 100)

print("Future Value: $" + str(int(FV * 100) / 100))