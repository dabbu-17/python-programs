import pandas as pd
# Create a sample employee DataFrame
data = {
'EmployeeID': [101, 102, 103, 104, 105],
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
'Age': [28, 32, 29, 35, 26]
}
df = pd.DataFrame(data)
# Display the initial DataFrame
print("Initial DataFrame:")
print(df)
# Let's say you want to delete the row for the employee named 'Charlie'
employee_to_delete = 'Charlie'
# Use the .loc property to delete the row based on the employee's name
df1 = df.loc[df['Name'] != employee_to_delete]
# Display the DataFrame after deleting the row
print("\nDataFrame after deleting the row for 'Charlie':")
#print(df)
print(df1)