'''Write a python program to calculate the area & circumference of a circle
from a diameter, taken aa user input value.
Print the output with proper messages.
A program should be well commented.
Variable names should follow the python variable naming conventions,
either use camel case or snake case'''

#taking the value of diameter from user
diameter =int(input("Enter Diameter of circle "))
#radius of circle = diameter/2
radius=diameter/2
#area of circle = 3.14*radius^2
area=3.14*(radius**2)
print("area of circle of diameter ", diameter , " is :",area)
#circumference of a circle= 2*3.14*radius
circumference=2*3.14*radius
print("circumference of circle of diameter ", diameter , " is :",circumference)
