# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.


import numpy as np
# Create arrays
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)

# Print arrays
print("Array of zeros:", zeros)
print("Array of ones:", ones)
print("Array of fives:", fives)