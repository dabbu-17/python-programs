# Function to calculate the net amount after discount
def cal_net_amount(product_code, order_amount):
    # Initialize discount to 0
    discount = 0
    
    # Check product code and apply discount based on order amount
    if product_code == 1:  # Battery-based toys
        if order_amount > 1000:
            discount = 0.10  # 10% discount
    elif product_code == 2:  # Key-based toys
        if order_amount > 100:
            discount = 0.05  # 5% discount
    elif product_code == 3:  # Electrical charging based toys
        if order_amount > 500:
            discount = 0.10  # 10% discount
    else:
        print("Invalid product code!")
        return None
    
    # Calculate the net amount
    net_amount = order_amount - (order_amount * discount)
    return net_amount

# Input product code and order amount
product_code = int(input("Enter product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging-based): "))
order_amount = float(input("Enter order amount: "))

# Calculate and display the net amount to be paid
net_amount = cal_net_amount(product_code, order_amount)

if net_amount is not None:
    print(f"The net amount to be paid after discount is: Rs. {net_amount:.2f}")
