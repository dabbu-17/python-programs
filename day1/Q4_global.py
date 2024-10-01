# Create a variable inside a function, with the same name as the global variable

var = "awesome"  #defining global variable

def myfunc():
  var = "fantastic"    #defining local variable with the same name as global
  print("Python is " + var)    #printing local variable

myfunc()

print("Python is " + var)     #printing global variable