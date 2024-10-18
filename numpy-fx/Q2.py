import numpy as np
# Monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
# Reshape array to 4 quarters with 3 months each
quarterly_sales = monthly_sales.reshape(4, 3)
# Print quarterly reports
for i, quarter in enumerate(quarterly_sales):
    print(f"Quarter {i+1}:")
    print("Monthly Sales:", quarter)
    print("Quarterly Total:", sum(quarter))
    print()