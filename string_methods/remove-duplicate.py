def remove_duplicate_words(input_string):

    words = input_string.split()
    unique_words = set()
    result = []

    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            result.append(word)

    return ' '.join(result)


# Test the function
input_string = "String and String Function"
output_string = remove_duplicate_words(input_string)

print("Input:", input_string)
print("Output:", output_string)
