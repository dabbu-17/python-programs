# Define the height of the pyramid
height = 5

# Iterate over each row
for i in range(1, height + 1):
    # Print leading spaces
    print(' ' * (height - i), end='')
    
    # Print stars
    print('*' * (2 * i - 1))
