import matplotlib.pyplot as plt

#Sample data for product sales
products = ['Laptop', 'Microoven', 'Smart phones', 'Smart watch', 'Dish Washer']
sales = [2500, 3000, 1500, 4000, 2200]

# Create a bar graph
plt.bar(products, sales, color='skyblue')

# Adding titles and labels
plt.title('Sales Comparison of Products in Q1')
plt.xlabel('Products')
plt.ylabel('Sales ')
plt.ylim(0, 4500)  # Set y-axis limits for better visibility

# Adding value labels on top of bars
for i, v in enumerate(sales):
    plt.text(i, v + 50, str(v), ha='center', fontsize=10)


# Show the graph
plt.grid(axis='y')
#plt.tight_layout()  # Adjust layout for better fit
plt.show()