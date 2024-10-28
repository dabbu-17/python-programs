'''Lab2: Create a pie chart to visualize the distribution of your monthly income by
source. You have collected data on the various sources of your income, such as
salary, freelance work, investments, and rental income. Share your
conclusion/analysis.
Input:
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]'''

import matplotlib.pyplot as plt

# Data for income sources and monthly income
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 6))
explode = (0.1, 0, 0, 0, 0)  # explode the Salary slice
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Monthly Income Distribution by Source')

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

# Conclusion/Analysis
# The pie chart illustrates the distribution of monthly income by source. 
# The salary slice is emphasized, indicating it constitutes the largest portion of the income, 
# followed by freelance work, while investments, rental income, and other sources 
# contribute a smaller percentage. This indicates a reliance on salary as the primary 
# source of income.



