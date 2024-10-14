'''
Write a Python program to count and display the vowels of a given text :-

String=”Welcome to python Training”
'''
string = "Welcome to python Training"
string = string.lower()
vowels = 'aeiou'
vowel_count = {vowel: 0 for vowel in vowels}

for char in string:
    if char in vowel_count:
        vowel_count[char] += 1

for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")








'''

Here are some professional ways to answer "Do you have a system to practice coding?":

*Yes, I have a system:*

1. "Yes, I regularly practice coding through online platforms like LeetCode, HackerRank, and CodeWars to stay up-to-date with industry trends and improve my problem-solving skills."
2. "I have a dedicated schedule for coding practice, utilizing tools like github and  Visual Studio Code to refine my skills in languages like Python, Java, and JavaScript."
3. "I participate in coding challenges and contests on platforms like Codeforces, CodinGame, and CodePen to continually enhance my coding abilities."



'''