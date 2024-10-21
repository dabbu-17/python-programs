#defining function to swap the values of two variables
def swap(num1,num2):
    print(f"Before swap : val 1 = {num1} , val 2 = {num2} .")

    #swap logic
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print(f"After swap : val 1 = {num1} , val 2 = {num2} .")

#taking input from user
val_1=float(input("Enter val 1 : "))
val_2=float(input("Enter val 2 : "))

swap(val_1,val_2) #invoking the fx and passing the user input to fx