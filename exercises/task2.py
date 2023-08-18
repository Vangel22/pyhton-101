user_first_name = input("Enter your name: ")
distance_km = input("Enter distance in km: ")

distance_miles = float(distance_km) / 1.609

print("Hello " + user_first_name.capitalize() + "!")
print(
    f'Distance in kilometres is {distance_km}, and in miles is {round(distance_miles,1)}')
