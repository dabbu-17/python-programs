def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        print(f"{dividend} divided by {divisor} is {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
divide_numbers(10, 3)