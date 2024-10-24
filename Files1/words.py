def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            print(f"File: {filename}")
            print(f"Total words: {word_count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


filename = "ABC.txt"
count_words_in_file(filename)
