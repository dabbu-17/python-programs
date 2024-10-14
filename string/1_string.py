'''
1. Write a Python program to count the occurrences of each word in a given sentence :-

string = “To change the overall look of your document. To change the look
available in the gallery”.
'''
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and split it into words
words = string.lower().replace(".", "").split()

# Create a dictionary to store the word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")
