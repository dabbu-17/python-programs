import matplotlib.pyplot as plt
months = ["January", "February", "March", "April", "May", "June"]
cakes_sold = [150,200,180,220,240,220]
plt.xlabel("months")
# ... existing code ...
plt.ylabel("cakes sold")
plt.bar(months, cakes_sold)
plt.show()