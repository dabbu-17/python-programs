import numpy as np
# Input array of temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 3.1, 38.7, 23.1, 1.5, 22.8, 37.2])
# Define temperature thresholds
hot_threshold = 35
cold_threshold = 5

hot_days = temperatures > hot_threshold
cold_days = temperatures < cold_threshold

# Combine hot and cold days into a single mask
extreme_days = np.logical_or(hot_days, cold_days)

# Print extreme days and corresponding temperatures
print("Extreme Days:")
print("Day Index:", np.where(extreme_days)[0])
print("Temperatures:", temperatures[extreme_days])

