print("\n")
portfolio_balance = float(input("Enter your portfolio balance: $"))

three_month_rate = float(input("Enter the current three-month-rate: "))
avg_benchmark_return = 8

ratio = (avg_benchmark_return - three_month_rate) / 10

cash_balance = portfolio_balance * (1 - ratio)
cash_balance = round(cash_balance, 2)

risk_balance = portfolio_balance - cash_balance

print(f"\nRecommended cash balance: ${cash_balance}")
print(f"Recommended risk balance: ${risk_balance}\n")