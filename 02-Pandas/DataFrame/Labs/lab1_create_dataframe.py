'''
Lab 1: Create a DataFrame
Question: Create a DataFrame from the following dictionary:
score = {'Math': [78, 85, 96, 80, 86],
         'English': [84, 94, 89, 83, 86],
         'Hindi': [86, 97, 96, 72, 83]}
'''

import pandas as pd
# Create a dictionary with the sample data
score = {
    'Math': [78, 85, 96, 80, 86],
    'English': [84, 94, 89, 83, 86],
    'Hindi': [86, 97, 96, 72, 83]
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(score)
# Display the DataFrame
print("DataFrame created from the dictionary:")
print(df)
