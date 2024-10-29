# Lab 3: Yearly Energy Consumption Analysis

import pandas as pd

# Input data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]

# Create Pandas Series for electricity and gas usage
electricity = pd.Series(data=electricity_usage, index=months, name='Electricity (kWh)')
gas = pd.Series(data=gas_usage, index=months, name='Gas (therms)')

# Display the Series
print("Lab 3: Monthly Energy Consumption")
print(electricity)
print("\n")
print(gas)
