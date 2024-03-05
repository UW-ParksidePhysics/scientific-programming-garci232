start_fahrenheit = 0
end_fahrenheit = 100
step = 10

print("°F            °C")

fahrenheit = start_fahrenheit
while fahrenheit <= end_fahrenheit:
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit}           {celsius:.2f}")
    fahrenheit += step