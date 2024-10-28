''' Create a bar chart to represent monthly expenses in different spending
categories and give your conclusion.
Input:
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
Monthly expenses in dollars (replace with your own data)
expenses = [1200, 400, 200, 150, 250]'''
import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color='lightcoral')

# Adding titles and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Categories')
plt.ylabel('Expenses in Dollars')
plt.ylim(0, max(expenses) + 300)  # Set y-axis limits for better visibility

# Show the plot
plt.grid(axis='y')
plt.show()

# Conclusion
# The bar chart visually represents the monthly expenses across different categories,
# highlighting that Rent is the largest expense, followed by Groceries and Transportation.
# This information can help in budgeting and identifying areas for potential savings.



