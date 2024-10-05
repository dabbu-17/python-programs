# Initialize a variable to store the sum of numbers
total_sum = 0
while True:
    # Ask the user to enter a number
    user_input = input("Enter a number (0 to stop): ")
    # Convert the user input to an integer
    num = int(user_input)
    # Check if the user entered 0
    if num == 0:
        # Break out of the loop if 0 is entered
        break
    # Add the entered number to the total sum
    total_sum += num
# Display the sum of all the numbers
print("Sum of entered numbers:", total_sum)