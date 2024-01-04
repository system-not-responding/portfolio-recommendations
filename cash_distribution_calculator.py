portfolio_balance = input("\nWhat's your portfolio balance?\n>>> $")
portfolio_balance = float(portfolio_balance)


three_month_rate = float(input("What's the current three-month-rate?\n>>> "))
avg_benchmark_return = 8

recommended_percent = (avg_benchmark_return - three_month_rate) / 10

cash_percent = portfolio_balance * recommended_percent
cash_percent = portfolio_balance - cash_percent
cash_percent = round(float(cash_percent), 2)
print(f"\nRecommended cash balance is: ${cash_percent}")

risk_percent = portfolio_balance - cash_percent
print(f"Recommended risk balance is: ${risk_percent}\n")


