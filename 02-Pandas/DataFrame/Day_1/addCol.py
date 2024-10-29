# Importing pandas library to work with DataFrames
import pandas as pd

# Creating a DataFrame with sample data
data = {
    'product_id': [101, 102, 103],
    'product_name': ['Laptop', 'Smartphone', 'Tablet'],
    'price': [1200, 800, 300]
}

# Initializing the DataFrame
df = pd.DataFrame(data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Storing the new column data in a separate list
# This list represents the stock quantity of each product
stock_data = [50, 100, 200]

# Adding a new column 'stock' to the DataFrame at index 1
# We will use the insert method to place the new column at index 1
df.insert(1, 'stock', stock_data)

# Printing the updated DataFrame with the new column
print("\nUpdated DataFrame with new 'stock' column at index 1:")
print(df)


