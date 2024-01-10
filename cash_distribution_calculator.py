print("\n")
portfolio_balance = float(input("Enter your portfolio balance: $"))

three_month_rate = float(input("Enter the current three-month-rate: "))
inflation_rate = float(input("Enter the current inflation rate: "))
avg_benchmark_return = 10.20   # 20year average yearly return for sp500

risk_free_rate = (avg_benchmark_return - three_month_rate) / avg_benchmark_return

cash_balance = portfolio_balance * (1 - risk_free_rate)
cash_balance = round(cash_balance, 2)
cash_pct = round((cash_balance / portfolio_balance) * 100, 2)

risk_balance = round(portfolio_balance - cash_balance, 2)
risk_pct = round((risk_balance / portfolio_balance) * 100, 2)

print(f"\nRecommended cash balance: ${cash_balance}/ {cash_pct}%")
print(f"Recommended risk balance: ${risk_balance}/ {risk_pct}%\n")
