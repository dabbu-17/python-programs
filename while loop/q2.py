num = int(input("Enter an integer: "))
original_num = num
reverse_num = 0
while num > 0:
    remainder = num % 10  # Get the last digit
    reverse_num = reverse_num * 10 + remainder  # Add it to the reverse_num
    num //= 10  # Remove the last digit from num

if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
