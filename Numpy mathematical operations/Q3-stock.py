'''3. Determine which products in a store are out of stock (quantity is 0).

 Input:

 inventory = np.array([10, 0, 5, 0, 20, 0])

 Output:

 Out of Stock Products: [0 0 0]

'''
import numpy as np

# Define the inventory array
inventory = np.array([10, 0, 5, 0, 20, 0])

# Determine which products are out of stock (quantity is 0)
out_of_stock = inventory[inventory == 0]

# Print the result
print("Out of Stock Products:", out_of_stock)

