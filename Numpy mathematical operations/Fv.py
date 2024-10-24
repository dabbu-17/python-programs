import numpy as np
# Simulated weather data (temperature in Celsius and rainfall in mm)
temperature = np.array([28, 32, 31, 29, 35, 26, 30])
rainfall = np.array([5, 0, 10, 0, 0, 8, 15])
# Identify hot days (temperature above 30°C) and rainy days (rainfall > 0 mm)
hot_days = temperature > 30
rainy_days = rainfall > 0
# Days that are both hot and rainy
hot_and_rainy_days =  np.logical_and(hot_days, rainy_days)
# Days that are either hot or rainy
hot_or_rainy_days =  np.logical_or(hot_days, rainy_days)
print("Hot Days:", hot_days)
print("Rainy Days:", rainy_days)
print("Hot and Rainy Days:", hot_and_rainy_days)
print("Hot or Rainy Days:", hot_or_rainy_days)
print("Day Index:", np.where(hot_or_rainy_days)[0])
