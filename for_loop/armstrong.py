def is_armstrong(n):
    # Convert to string to find the number of digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Initialize sum
    sum_of_digits = 0
    
    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    return n == sum_of_digits


# Test the function
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")