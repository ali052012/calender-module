
# Function to calculate hotel cost
def hotel_cost(nights):
    return 140 * nights

# Function to calculate plane ride cost based on destination
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0  # unknown city

# Function to calculate rental car cost based on number of days
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

# Function to calculate total trip cost
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

# Example usage
print("Cost of car rental:", rental_car_cost(5))
print("Cost of plane ride:", plane_ride_cost("Los Angeles"))
print("Cost of hotel room:", hotel_cost(7))
print("Total cost of the trip:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 500))
