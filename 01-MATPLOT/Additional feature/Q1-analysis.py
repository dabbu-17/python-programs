'''Lab1: Analyze the relationship between the size of houses (measured in square
footage) and their selling prices in a particular neighborhood. You have collected
data on various houses in that neighborhood.Create a scatter plot using the
below data and share your conclusion/analysis.
Input:
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])'''

import numpy as np
import matplotlib.pyplot as plt

# Data for square footage and selling prices
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create a scatter plot
plt.scatter(square_footage, selling_prices, color='blue', marker='o')

# Adding title and labels
plt.title('House Size vs Selling Price')
plt.xlabel('Square Footage')
plt.ylabel('Selling Price (in thousands)')

# Show the plot
plt.grid(True)
plt.show()

# Conclusion/Analysis
# As the square footage of the houses increases, the selling prices tend to increase as well. 
# This indicates a positive correlation between the size of the house and its selling price.

