# Function to count letters, digits, and special symbols in a string
def count_characters(input_string):
    # Initialize counters for letters, digits, and special symbols
    letter_count = 0
    digit_count = 0
    special_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            letter_count += 1
        # Check if the character is a digit
        elif char.isdigit():
            digit_count += 1
        # If it's neither a letter nor a digit, it is a special symbol
        else:
            special_count += 1
            
    # Return the counts as a dictionary
    return {
        "letters": letter_count,
        "digits": digit_count,
        "special_symbols": special_count
    }

# Input string
input_string = "P@#yn26at^&i5ve"

# Call the function and store the result
result = count_characters(input_string)

# Print the results
print("Count of letters:", result["letters"])
print("Count of digits:", result["digits"])
print("Count of special symbols:", result["special_symbols"])
