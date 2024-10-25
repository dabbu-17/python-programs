# Define two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Use symmetric difference operation to get elements in set1 or set2, but not both
unique_elements = set1.symmetric_difference(set2)

# Print the unique elements
print("Unique elements:", unique_elements)