def display_words(filename):
    try:
        with open(filename, 'r') as file:
            short_words = [word for line in file for word in line.split() if len(word) < 4]
            print(short_words)
            print("Total Short Words =",len(short_words))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


filename = "story.txt"
display_words(filename)