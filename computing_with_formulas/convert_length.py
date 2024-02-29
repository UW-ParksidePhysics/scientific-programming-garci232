one_inch = 2.54 # centimeters
one_foot = 12 # inches
one_yard = 3 #feet
one_mile = 1760 #yards
distance_home_to_campus = 10.7 # miles
km_to_mile = 1.609 # kilometers
distance_home_to_campus_in_km = distance_home_to_campus * km_to_mile
print(distance_home_to_campus_in_km
     )
distance_home_to_campus_in_inches = distance_home_to_campus_in_km * one_inch
print(distance_home_to_campus_in_inches)

distance_home_to_campus_in_feet = distance_home_to_campus_in_inches / one_foot
print(distance_home_to_campus_in_feet)

distance_home_to_campus_in_yards = distance_home_to_campus_in_feet / one_yard
print(distance_home_to_campus_in_yards)

distance_home_to_campus_in_miles = distance_home_to_campus_in_yards / one_mile
print(distance_home_to_campus_in_miles)