'''
Write a Python program to reverse words in a string :-

String = “Deeptech Python Training”
'''

string = "Deeptech Python Training"
words = string.split()
reversed_words = ' '.join(reversed(words))
print(reversed_words)
