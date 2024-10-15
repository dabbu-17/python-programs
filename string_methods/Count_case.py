def count_characters(input_string):
    uppercase = sum(1 for c in input_string if c.isupper())
    lowercase = sum(1 for c in input_string if c.islower())
    special_chars = sum(1 for c in input_string if not c.isalnum())
    numeric = sum(1 for c in input_string if c.isdigit())

    print("Input String:", input_string)
    print("Uppercase Letters:", uppercase)
    print("Lowercase Letters:", lowercase)
    print("Special Characters:", special_chars)
    print("Numeric Values:", numeric)


input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_characters(input_string)