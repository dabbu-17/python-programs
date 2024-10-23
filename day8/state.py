''' Define a method that takes in as a parameter state capital pairs as a
single string where in the string the pairs will be separated by a '-'
and in each pair the state will be separated from the capital by a '|'.
The method should output each state capital pair in a new line. '''
def state_capital(list):
    pair_list = list.split('-')  # Split the input string into pairs
    for pair in pair_list:  # Iterate over each pair
        state, capital = pair.split('|')   # Split the pair into state and capital
        print(state, capital)  # Print the state and capital
str = "Bihar|Patna-WB|Kolkata-UP|Lucknow-Karnataka|Bengaluru"
state_capital(str)  