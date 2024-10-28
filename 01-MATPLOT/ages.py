import matplotlib.pyplot as plt
import numpy as np

# Sample data: ages of 100 attendees
ages = [22, 25, 30, 22, 26, 27, 30, 31, 29, 35,
        40, 22, 23, 24, 29, 35, 30, 34, 40, 45,
        28, 29, 31, 22, 30, 36, 24, 23, 22, 25,
        40, 41, 42, 39, 38, 37, 36, 33, 35, 32,
        28, 25, 21, 19, 22, 24, 29, 27, 31, 32,
        41, 45, 50, 29, 28, 27, 24, 26, 30, 35,
        36, 40, 42, 45, 48, 51, 55, 60, 64, 68,
        70, 75, 80, 85, 90, 92, 95, 100, 22, 23,
        26, 29, 28, 27, 22, 23, 25, 30, 35, 33]

# Create a histogram
plt.hist(ages, bins=np.arange(10, 110, 10), color='lightblue', edgecolor='black')

# Adding titles and labels
plt.title('Age Distribution of Community Event Attendees')
plt.xlabel('Age')
plt.ylabel('Number of Attendees')

# Show the graph


plt.xticks(np.arange(10, 110, 10))  # Set x-ticks for clarity
plt.tight_layout()  # Adjust layout for better fit
plt.grid(axis='both')  # Show grid for both x and y axes
plt.show()