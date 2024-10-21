#defining function to check no is positive or negative
def check_no(a):
    if a>0: #to check if its +ve
        print(f"{a} is positive number.")
    elif a<0: #to check if its -ve
        print(f"{a} is negative number.")
    else: #to check if its 0
        print(f"{a} is 0 , i.e neither positive nor negative .")
        

check_no(user_input) #invoking fx and passing the user input to fx