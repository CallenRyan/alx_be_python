monthly_income = 5000 
monthly_expenses = 4000 
monthly_savings = monthly_income - monthly_expenses 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) 
print(f"Your monthly savings are ${monthly_savings:.2f}.") 
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.") 
