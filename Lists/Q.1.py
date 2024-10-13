# Q.1. Write a Python program to sum all the items in a list.

#Calling the Function to sum all the items in a list
def sum_of_list(numbers):
    return sum(numbers)

# Example list
numbers = [10, 20, 30, 40, 50]

# Calling the function and print the result
total = sum_of_list(numbers)
print(f"The sum of the list items is: {total}")
