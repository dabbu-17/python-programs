import pandas as pd
# Provide the path to your CSV file
csv_file_path = '02-Pandas\DataFrame\Conditional queries on Data\customer_data.csv' # Replace with the actual path to your CSV file
col=['Transaction_ID','Gender','Age','Marital_status','Payment_method',
'Amount_spent' ]
# Use read_csv to read the data from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path,usecols=col)
# filtering - Only show Paypal users
condition = df['Payment_method'] == 'PayPal'
# display top 4 rows
print(df[condition].head(4))