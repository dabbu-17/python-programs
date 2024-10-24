def count_uppercase_chars_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for c in text if c.isupper())
            print(f"File: {filename}")
            print(f"Total uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
filename = "ABC.txt"
count_uppercase_chars_in_file(filename)