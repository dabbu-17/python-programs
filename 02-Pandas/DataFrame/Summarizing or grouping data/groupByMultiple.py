import pandas as pd
# Provide the path to your CSV file
csv_file_path = '02-Pandas\DataFrame\Summarizing or grouping data\customer_data.csv' # Replace with the actual path to your CSV file
# Use read_csv to read the data from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
#Group By multiple columns
state_gender_res =df[['State_names','Gender','Payment_method','Amount_spent']].groupby(['State_names','Gender', 'Payment_method']).agg(['count', 'min', 'max'])
# fetch top 12 records meeting the above condition
print(state_gender_res.head(12))
