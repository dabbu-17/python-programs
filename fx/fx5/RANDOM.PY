import random
# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
# Display the generated numbers
print("Generated numbers:", random_numbers)
# Find and display the maximum number
max_number = max(random_numbers)
print("Maximum number:", max_number)
# Find and display the minimum number
min_number = min(random_numbers)
print("Minimum number:", min_number)