import pandas as pd
# Provide the path to your CSV file
csv_file_path = '02-Pandas\DataFrame\Summarizing or grouping data\customer_data.csv' # Replace with the actual path to your CSV file
# Use read_csv to read the data from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
print(df[['Age', 'Amount_spent']].groupby(df['Gender']).max())
