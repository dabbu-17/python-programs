#program to rename the column names of the dataframe

import pandas as pd

#creating a dataframe
df = pd.DataFrame({
    'product_id': [101, 102, 103],
    'product_name': ['Laptop', 'Smartphone', 'Tablet'],
    'stock': [50, 100, 200],
    'price': [1200, 800, 300]
})

#printing the original dataframe
print("Original DataFrame:")
print(df)

#renaming the column names
df.columns = ['id', 'name', 'quantity', 'cost']

#printing the updated dataframe
print("\nUpdated DataFrame:")
print(df)

        
