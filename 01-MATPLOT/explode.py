import matplotlib.pyplot as plt

# Market share data
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Others']
market_share = [30, 25, 18, 12, 15]
# Colors for each slice
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']
# Explode the 'Apple' slice
explode = (0.1, 0.2, 0.3, 0.1, 0)  # Multiple slices are exploded

# Create a pie chart
plt.pie(market_share, labels=manufacturers, colors=colors, explode=explode, autopct='%1.1f%%')

# Title
plt.title('Smartphone Market Share')

# Show the pie chart
plt.show()