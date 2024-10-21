# Function to calculate the fare based on the distance
def calculate_fare(distance):
    if distance <= 50:
        return distance * 8
    elif distance <= 100:
        return (50 * 8) + ((distance - 50) * 10)
    else:
        # Calculate the fare for the first 50 km at 8 Rs./Km
        # the next 50 km at 10 Rs./Km, and the remaining distance at 12 Rs./Km
        return (50 * 8) + (50 * 10) + ((distance - 100) * 12)

# Get the distance from the user
distance = int(input("Enter the distance in km: "))

# Calculate and print the fare
print("Fare: ₹", calculate_fare(distance))

 