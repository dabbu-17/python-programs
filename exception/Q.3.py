'''Q.3. Write a Python program that opens a file and handles a FileNotFoundError exception
if the file does not exist.'''
# Function to open a file and read its contents
def open_file(file_name):
    try:
        # Attempt to open the file in read mode
        with open(file_name, 'r') as file:
            # Read and print the file contents
            content = file.read()
            print(content)
    except FileNotFoundError:
        # If the file does not exist, this block handles the error
        print(f"Error: The file '{file_name}' was not found.")

# Taking input from user
file_name = input("Enter the name of the file to open: ")
# Calling the function to open file
open_file(file_name)
