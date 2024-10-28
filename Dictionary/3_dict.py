'''
3.Write a Python program to get the key, value and item in a dictionary.

input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dict_num={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
    