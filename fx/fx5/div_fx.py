'''
1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
'''
def div(dividend,divisor):
    if divisor != 0:
      result = dividend / divisor
      print(f"{dividend} / {divisor} = {result:.2f}")
    else:
       print("Error: Division by zero is not allowed")

divi = float(input("Enter the dividend : ")) #taking dividend from user
divs = float(input("Enter the divisor : ")) #taking divisor from user
div(divi,divs)

