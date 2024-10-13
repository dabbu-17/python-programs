# Q.3. Write a Python program to find duplicate values from a list and display those.

# Creating a function to find and display duplicate values in a list
def find_duplicates(numbers):
    duplicates = []  # List to store duplicate values
    unique_numbers = [] 
    # Using for loop to find duplicates number
    for num in numbers:
        if num in unique_numbers and num not in duplicates:
            duplicates.append(num)  # Add to duplicates if it's already seen
        else:
            unique_numbers.append(num)  # Track the number if it's new
    #return the value
    return duplicates
# Making the list
numbers = [4, 5, 6, 7, 4, 5, 9, 10, 6, 5]
# Calling the function and print the result
duplicates = find_duplicates(numbers)
print(f"The duplicate values are: {duplicates}")
