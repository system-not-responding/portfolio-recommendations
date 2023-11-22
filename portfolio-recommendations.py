import pandas as pd

portfolio_balance = input("\nWhat's your portfolio balance? $")
portfolio_balance = float(portfolio_balance)
print(f"Your portfolio's current balance is: ${portfolio_balance}")

recommended_percent = .3
cash_percent = portfolio_balance * recommended_percent
cash_percent = portfolio_balance - cash_percent
cash_percent = round(float(cash_percent), 2)
print(f"The current recommended cash balance is: ${cash_percent}")

risk_percent = portfolio_balance - cash_percent
print(f"Your recommened risk balance is: ${risk_percent}\n")


