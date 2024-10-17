'''
3. Write a Python program to calculate the sum of the numbers in a given tuple.

Input: tuples_list = [(1, 2), (3, 4), (5, 6)]

Output:
'''
tuples_list = [(1, 2), (3, 4), (5, 6)]
sum=sum(sum(tup) for tup in tuples_list)
print("Output :", sum)
