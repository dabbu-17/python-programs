# Define two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Check if sets have common elements ,  
# The `&` operator performs an intersection operation, returning a new set containing elements common to both `set1` and `set2`. 
if set1 & set2:
    print("Common elements:", set1 & set2)
else:
    print("No common elements.")
