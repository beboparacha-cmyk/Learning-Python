def hotel_cost(nights):
    return 140+nights

def plane_ride_cost(city):
    if "Dubai" == city:
        return 210
    elif "Saturn" == city:
        return 1000000000000
    elif "BlackHole" == city:
        return 1000000000000000000000000
    elif "Village" == city:
        return 20
    
def rental_car_cost(days):
    if days>=7 :
        return 40+days - 50
    elif days>=3 :
        return 40+days - 20
    else:
        return 40+days
    
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental:",rental_car_cost(5))
print("Cost of plane ride:",plane_ride_cost("Saturn"))
print("Cost of hotel room:",hotel_cost(7))
print("Total cost of the trip:",trip_cost("Saturn",1000000000000))
print(trip_cost("Village",20))