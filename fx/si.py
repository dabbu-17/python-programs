# Define the principal amount, rate, and time
principal = 200
rate = 5  # in percentage
time = 5  # in years

# Calculate the Simple Interest
simple_interest = (principal * rate * time) / 100

# Print the result
print(f"Principal: Rs. {principal}")
print(f"Rate: {rate}% per year")
print(f"Time: {time} years")
print(f"Simple Interest: Rs. {simple_interest:.2f}")
print(f"Total Amount: Rs. {principal + simple_interest:.2f}")