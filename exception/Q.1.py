# Q.1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Creating a function to handle zerodivisionerror exception
def zero_division(numerator,denominator):
    try:
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# taking input form user
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Calling the function 
zero_division(num1, num2)