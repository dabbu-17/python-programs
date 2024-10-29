# Import the pandas library, which provides powerful data manipulation and analysis tools
import pandas as pd

# Specify the path to the CSV file containing customer data
csv_file_path = '02-Pandas\DataFrame\Files\customer_data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Print unique values in the 'State_names' column
print(df['State_names'].unique())

# Store unique values of 'State_names' in a variable
unique_df = df['State_names'].unique()

# Print the number of unique states
print(len(unique_df))

# Print the count of occurrences for each unique state
print(df['State_names'].value_counts())

# Print the count of occurrences for each unique gender
print(df['Gender'].value_counts())
csv_file_path = '02-Pandas\DataFrame\Files\customer_data.csv'
df = pd.read_csv(csv_file_path)

print(df['State_names'].unique())
unique_df=df['State_names'].unique()
print(len(unique_df))
print(df['State_names'].value_counts())
print(df['Gender'].value_counts())

