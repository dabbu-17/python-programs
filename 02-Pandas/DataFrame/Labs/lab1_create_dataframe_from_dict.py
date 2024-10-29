import pandas as pd

# Sample data
score = {'Math': [78, 85, 96, 80, 86], 'English': [84, 94, 89, 83, 86], 'Hindi': [86, 97, 96, 72, 83], 'Science': [90, 88, 92, 85, 87], 'Social Studies': [82, 91, 88, 85, 89]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(score)

# Display the DataFrame
print("DataFrame created from the dictionary:")
print(df)
