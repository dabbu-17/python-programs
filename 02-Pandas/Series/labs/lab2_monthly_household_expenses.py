# Lab 2: Monthly Household Expenses Analysis

import pandas as pd

# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series with expense categories as index and amounts as values
monthly_expenses = pd.Series(data=expenses, index=categories, name='Monthly Expenses (USD)')

# Display the Series
print("Lab 2: Monthly Household Expenses")
print(monthly_expenses)

# ... (rest of the code remains the same)
