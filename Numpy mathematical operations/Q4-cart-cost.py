''' 4.Calculate the total cost of items in a shopping cart, considering the quantity and price

 per item.

 Input:

 quantity = np.array([2, 3, 4, 1])

 price_per_item = np.array([10.0, 5.0, 8.0, 12.0])

 Output:

 Total Cost of Items: [20. 15. 32. 12.]'''
import numpy as np

# Define the quantity and price per item arrays
quantity = np.array([2, 3, 4, 1])
price_per_item = np.array([10.0, 5.0, 8.0, 12.0])

# Calculate the total cost of items
total_cost = quantity * price_per_item

# Print the result
print("Total Cost of Items:", total_cost)
