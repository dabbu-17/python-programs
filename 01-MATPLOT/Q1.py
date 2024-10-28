'''Visualize the daily temperature changes over time in a city and give your conclusion
Input:
days = list(range(1, 32))
# Daily temperature data (replace with your own data)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78,
80, 81, 82, 83, 82, 80, 78, 76, 74, 71]'''
import matplotlib.pyplot as plt
# Data
days = list(range(1, 32))
# Collect maximum temperature of Greater Noida of past 31 days
temperature = [20, 22, 19, 23, 21, 18, 24, 22, 20, 25, 23, 21, 19, 24, 22, 20, 23, 21,
                18, 25, 22, 24, 19, 23, 21, 20, 24, 22, 19, 25, 23]

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')

# Display the plot
plt.grid(True)
plt.show()

# Conclusion
# The temperature generally increases from the beginning to the middle of the month, peaking around day 25,
# and then gradually decreases towards the end of the month.
# This pattern suggests a typical warming trend followed by a cooling trend within the month.
