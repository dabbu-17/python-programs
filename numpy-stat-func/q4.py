import numpy as np

#1. Read the data from the CSV file into a Nuny array, skipping the header rou try:
try:
    house_prices = np.genfromtxt("house prices.csv", delimiter="", skip_header=1) 
except IOError:
   print("Error: File not found or unable to read data.")
   house_prices = np.array([])
# 2. Remove nav values if any
house_prices = house_prices[~np.insane(house_prices)]

#3. Calculate the average of house prices
if house_prices.size> 0:
    average_price = np.mean(house_prices) 
    print("Average house price:", average_price)

    #4. Ideaverage highntify house prices above the average
    high_prices = house_prices[house_prices > average_price] 
    print("House prices above average:", high_prices)          
    #5. Save the list of high prices to a new CSV file 
    np.savetxt("high prices.csv", high_prices, delisiter=',') 
    print("High prices saved to high prices.csv")
else:
    print("No valid house prices data available.")