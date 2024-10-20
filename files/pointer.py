#Creating a class 'Point'
class Point:
    #Defining a constructor function for the class
    def __init__(self,xCoord,yCoord):
        self.xCoord=xCoord
        self.yCoord=yCoord

    #Defining a method for printing the point location
    def printPointLocation(self):
        print("The point is located at (",self.xCoord,",",self.yCoord,")")

#Creating an object of the class 'Point'

point =Point(2.5,3.5)

#Printing the point location
point.printPointLocation()