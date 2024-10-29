import pandas as pd

def weekly_sales():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sales_data = [300, 450, 500, 600, 700, 800, 900]
    series = pd.Series(sales_data, index=days)
    print(series)

weekly_sales()  # Call the function to display weekly sales

