# Define two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Remove items from set1 that are not common to both sets
set1 &= set2

# Print the updated set1
print("Common elements:", set1)