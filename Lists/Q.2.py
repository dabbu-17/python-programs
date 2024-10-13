# Q.2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# Creating the function to find largest and smallest numbers in a list
def find_number_type(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    # Using for loop to find the largest and smallest numbers
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    # Return the value
    return largest, smallest
# Creating list
numbers = [45, 3, 67, 23, 90, 1, 77]

# Calling the function and print the result
largest, smallest = find_number_type(numbers)
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
