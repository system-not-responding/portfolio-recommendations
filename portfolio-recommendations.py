portfolio_balance = input("\nWhat's your portfolio balance?\n>>> $")
portfolio_balance = float(portfolio_balance)

recommended_percent = .3
cash_percent = portfolio_balance * recommended_percent
cash_percent = portfolio_balance - cash_percent
cash_percent = round(float(cash_percent), 2)
print(f"\nRecommended cash balance is: ${cash_percent}")

risk_percent = portfolio_balance - cash_percent
print(f"Recommened risk balance is: ${risk_percent}\n")

