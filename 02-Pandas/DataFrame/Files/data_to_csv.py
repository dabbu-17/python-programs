import pandas as pd
# Create a Pandas DataFrame
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
# Specify the file path to save the CSV file
csv_file_path = '02-Pandas/DataFrame/Files/output.csv'
# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False) # this will create a new file in the current folder
print(f'Data has been written to {csv_file_path}')
