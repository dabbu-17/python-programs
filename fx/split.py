#The string contains a list of fruits separated by ',' as the delimeter
line="grape guava mango watermelon apple"
#Splits the line into individual substrings and returns a list of the substrings
fruits=line.split(" ")
#Printing the list
print(fruits)
for fruit in fruits:
    print(f"I like  {fruit} ")