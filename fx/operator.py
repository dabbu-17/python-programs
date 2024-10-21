# Function to perform arithmetic operations
def arithmetic_operations(a, b):
    print(f"First number: {a}")
    print(f"Second number: {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} * {b} = {a * b}")

# Input values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to display arithmetic operations
arithmetic_operations(num1, num2)