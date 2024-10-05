# Ask the user to enter a number
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial result
factorial = 1

# Initialize a counter variable
i = 1

# Start a while loop that continues until i is less than or equal to num
while i <= num:
    # Multiply the current factorial result by the current counter value
    factorial *= i
    
    # Increment the counter by 1
    i += 1

# Print the final factorial result
print("Factorial of", num, "is", factorial)