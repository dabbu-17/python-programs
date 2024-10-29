# Importing pandas library to work with DataFrames
import pandas as pd

# Creating a DataFrame with sample data
data = {
    'product_id': [101, 102, 103],
    'product_name': ['Laptop', 'Smartphone', 'Tablet'],
    'stock': [50, 100, 200],
    'price': [1200, 800, 300]
}

# Initializing the DataFrame
df = pd.DataFrame(data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Creating a dictionary for the new row data
new_row = {'product_id': 104, 'product_name': 'Pineapple', 'stock': 75, 'price': 250}

# Converting the new row dictionary to a DataFrame
new_row_df = pd.DataFrame([new_row])

# Adding the new row at index 2
df = pd.concat([df.iloc[:2], new_row_df, df.iloc[2:]]).reset_index(drop=True)

# Printing the updated DataFrame with the new row at index 2
print("\nUpdated DataFrame with new row at index 2:")
print(df)

# Alternatively, you can use the append method (deprecated in newer versions of pandas)
# df = df.append(new_row, ignore_index=True)

# If you want to add the new row at a specific position, you can use the insert method
# new_row_series = pd.Series(new_row)
# df = pd.concat([df.iloc[:2], new_row_series.to_frame().T, df.iloc[2:]]).reset_index(drop=True)

# Print the DataFrame if using one


