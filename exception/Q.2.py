'''Q.2. Write a Python program that prompts the user to input an integer and raises a 
ValueError exception if the input is not a valid integer.'''

# Creating the Function to get a valid integer from the user
def get_integer():
    try:
        user_input = input("Please enter an integer: ")
        # Convert the input to an integer
        user_input = int(user_input)
        
        # If the conversion is successful, print the integer
        print(f"You entered the integer: {user_input}")
    except ValueError:
        # If the input cannot be converted to an integer, raise ValueError
        print("Please enter a valid integer.")

# Calling the function to test
get_integer()
