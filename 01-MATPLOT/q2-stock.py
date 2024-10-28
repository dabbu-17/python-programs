''' Create a line plot to visualize the daily closing prices of a stock over a year

and give your conclusion.

Input:

days = list(range(1, 78))

# Daily closing prices of a stock (replace with your own data)

stock_prices = [100, 105, 110, 115, 112, 120,

118, 125, 128, 130, 132, 135,

138, 140, 142, 144, 145, 148,

150, 155, 160, 158, 162, 165,

170, 172, 175, 178, 180, 182,

185, 188, 190, 192, 195, 198,

200, 198, 195, 193, 190, 188,

185, 182, 180, 178, 175, 172,

170, 168, 165, 162, 160, 158,

155, 152, 150, 148, 145, 143,

140, 138, 135, 132, 130, 128,

125, 123, 120, 118, 115, 112,

110, 108, 105, 103, 100]

'''
import matplotlib.pyplot as plt

# Data
days = list(range(1, 78))
stock_prices = [100, 105, 110, 115, 112, 120,
                118, 125, 128, 130, 132, 135,
                138, 140, 142, 144, 145, 148,
                150, 155, 160, 158, 162, 165,
                170, 172, 175, 178, 180, 182,
                185, 188, 190, 192, 195, 198,
                200, 198, 195, 193, 190, 188,
                185, 182, 180, 178, 175, 172,
                170, 168, 165, 162, 160, 158,
                155, 152, 150, 148, 145, 143,
                140, 138, 135, 132, 130, 128,
                125, 123, 120, 118, 115, 112,
                110, 108, 105, 103, 100]

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(days, stock_prices, color='blue', linewidth=2)

# Add labels and title
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Daily Closing Prices of a Stock Over a Year')

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()

# Conclusion
'''
The stock price shows an overall upward trend for the first half of the year,
reaching a peak around day 37. After this peak, there's a gradual decline
for the rest of the year, ending at approximately the same price it started.
This pattern suggests a bullish market in the first half, followed by a
bearish trend in the second half of the year. Investors might want to
consider this cyclical behavior for future trading strategies.
'''
