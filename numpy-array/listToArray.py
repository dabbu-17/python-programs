'''4. Write a NumPy program to convert a list and tuple into arrays.
   Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8]
   Input: my_tuple = ([8, 4, 6], [1, 2, 3]) '''

import numpy as np
# Define the list and tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])
# Convert list to array
list_array = np.array(my_list)
# Convert tuple to array
tuple_array = np.array(my_tuple)
# Print the results
print("List Array:", list_array)
print("Tuple Array:\n", tuple_array)