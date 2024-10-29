import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales_data = [1500, 2000, 2500, 3000, 3500, 4000, 
                         4500, 5000, 5500, 6000, 6500, 7000]
series = pd.Series(sales_data, index=months)
print(series)


