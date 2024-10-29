"""
Lab 3: Write a Pandas program to drop the rows where all elements are missing in a given DataFrame.

Input:
df = pd.DataFrame({
'ord_no':[np.nan,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[np.nan,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
'ord_date': [np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[np.nan,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001]})
"""

import pandas as pd
import numpy as np
# Create the sample DataFrame with some fully missing rows
df = pd.DataFrame({
    'ord_no': [np.nan, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [np.nan, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': [np.nan, '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10',
                  '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [np.nan, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001]
})
# Function to drop rows where all elements are missing
def drop_rows_all_missing(dataframe):
    # Use dropna() with how='all' to remove rows where all values are missing
    cleaned_df = dataframe.dropna(how='all')
    return cleaned_df
# Drop rows with all missing values and display the result
result = drop_rows_all_missing(df)
print("DataFrame after dropping rows with all missing values:")
print(result)
# Display the number of rows before and after dropping
print(f"\nNumber of rows before dropping: {len(df)}")
print(f"Number of rows after dropping: {len(result)}")
