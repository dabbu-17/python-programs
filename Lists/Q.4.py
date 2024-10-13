'''Q.4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:[1, 1, 2, 3, 4, 4, 5, 1] , Length of the first part of the list: 3 , 
Splitted the said list into two parts:([1, 1, 2], [3, 4, 4, 5, 1])'''
# Creating the Function to split a list into two parts
def split_list(original_list, length_of_first_part):
    # Split the list into two parts
    first = original_list[:length_of_first_part]
    second = original_list[length_of_first_part:]
    #return the value
    return first, second
# Using given list and specified length
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
# Calling the function to split the list
first, second = split_list(original_list, length_of_first_part)
# Print the results
print(f"Original list: {original_list}")
print(f"Length of the first part of the list: {length_of_first_part}")
print(f"Splitted the said list into two parts: ({first}, {second})")
