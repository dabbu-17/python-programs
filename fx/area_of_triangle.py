# Write a program to input 3 sides of a triangle and calculate and print its area.


# Get the lengths of the three sides of the triangle from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if the input sides can form a valid triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    # Calculate the semi-perimeter of the triangle
    semi_perimeter = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

    # Print the area
    print("The area of the triangle is:", area)
else:
    print("The input sides cannot form a valid triangle.")