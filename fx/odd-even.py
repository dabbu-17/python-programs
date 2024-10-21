#defining function to check no is even or odd
def check_no(a):
    if a==0 : #to check if its 0
        print(f"{a} is neither even nor odd .")
    elif a%2==0: #to check if its even
        print(f"{a} is even number.")
    else: #to check if its odd
        print(f"{a} is odd number.")

user_input = int(input("Enter the number: ")) #taking input from user

check_no(user_input) #invoking fx and passing the user input to fx