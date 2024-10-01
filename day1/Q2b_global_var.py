#defining global variable

def myfunc():  #defining function
  global x   #defining x as global var
  x = "nice"   #initializing value of x

myfunc()

print("Python is " + x) #printing global var outside function