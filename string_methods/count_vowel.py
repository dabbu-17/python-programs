def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = sum(1 for c in input_string if c in vowels)
    print("Input String:", input_string)
    print("Total vowels are:", count)


input_string = "Welcome to Python Assignment"
count_vowels(input_string)