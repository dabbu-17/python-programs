'''
1. Write a Python program and calculate the mean of the below dictionary.

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

Output: 6.2
'''
dict={"A":6, "B":9, "C":5, "D":7, "E":4}
sum=sum(dict.values())
items=len(dict)
value=sum/items
print(f"The mean of the dictionary value is : {value}")
