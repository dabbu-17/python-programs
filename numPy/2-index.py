import numpy as np
# Define the list
my_list = [1, 2, 3, 4, 5]
# Convert the list to a NumPy array
my_array = np.array(my_list)
# Display the array
print(f"Original Array:\n {my_array}")
# Display the first and last index
print(f"\nFirst Index: {my_array[0]}")
print(f"Last Index: {my_array[-1]}")
# Multiply each element and print the result
print(f"\nArray after multiplication:{my_array*2}")