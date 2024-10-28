import matplotlib.pyplot as plt

days = list(range(1, 8))
temperature = [65, 68, 70, 72, 75, 76, 78]

plt.plot(days, temperature)
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Changes Over Days')
plt.show()
