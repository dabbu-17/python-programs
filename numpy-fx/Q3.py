import numpy as np
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
# Days since last purchase
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
# Split customers into two groups
recent_customers = customer_ids[last_purchase_days_ago <= 30]
inactive_customers = customer_ids[last_purchase_days_ago > 30]
# Print results
print("Recent Customers (last 30 days):", recent_customers)
print("Inactive Customers (more than 30 days):", inactive_customers)