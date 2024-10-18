import numpy as np 
try:
    house_prices = np.genfromtxt("house_prices.csv", skip_header=1) 
except IOError:
   print("Error: File not found.")
   house_prices = np.array([])
# 2. Remove NaN values if any
house_prices = house_prices[~np.isnan(house_prices)]
# 3. Calculate the average of house prices
if house_prices.size > 0:
    average_price = np.mean(house_prices) 
    print("Average of the house prices is:", average_price)
    # 4. Identify house prices above the average
    high_prices = house_prices[house_prices > average_price] 
    print("House prices above average:", high_prices)          
    # 5. Save the list of high prices to a new CSV file 
    np.savetxt("high_prices.csv", high_prices) 
    print("High prices are saved into high_prices.csv")
else:
    print("There is No valid house prices data available.")
