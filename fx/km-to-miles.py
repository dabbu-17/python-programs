#defining a function to convert kilometer to miles 
def km_to_miles(km):
    if km<0: #to check if entered value is valid or not ,(km cant be -ve)
        print("Enter valid value. ")
    else:
        miles=km *0.621371 #formula of converting km to miles,i.e 1km= 0.621371 miles
        print(f"{km} kilometer = {miles:.2f} miles")

user_input=float(input("Enter Value in  kilometer :")) #taking input from user

km_to_miles(user_input) #invoking the fx and passing the user input to fx

