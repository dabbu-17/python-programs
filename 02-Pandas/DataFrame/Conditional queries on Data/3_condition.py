import pandas as pd
# Provide the path to your CSV file
csv_file_path = '02-Pandas\DataFrame\Conditional queries on Data\customer_data.csv' # Replace with the actual path to your CSV file
col=['Gender','State_names','Age','Marital_status','Payment_method', 'Amount_spent'
]
# Use read_csv to read the data from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path,usecols=col)
# first create 3 condition
female_person = df['Gender'] == 'Female'
married_person = df['Marital_status'] == 'Married'
loc_newyork = df['State_names'] == 'New York'
# we passing condition on our dataframe
# printing top 4 records meeting the above criteria
print(df[female_person & married_person & loc_newyork].head(4))