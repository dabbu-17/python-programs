'''Q.4. Write a Python program that prompts the user to input two numbers and
raises a TypeError exception if the inputs are not numerical'''

# Creating a Function to get user input and ensure both inputs are numbers
def get_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        #converting the inputs to floats
        num1 = float(num1)
        num2 = float(num2)
        # If conversion is successful, print the two numbers
        print(f"The two numbers you entered are: {num1} and {num2}")
    except ValueError:
        # Raising a TypeError if the input values are not numeric
        raise TypeError("Error: Both inputs must be numerical values.")
# Calling the function
get_numbers()
