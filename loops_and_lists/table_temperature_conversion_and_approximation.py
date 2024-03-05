start_fahrenheit = 0
end_fahrenheit = 100
step = 10

print("°F       °C       T^c")

fahrenheit = start_fahrenheit
while fahrenheit <= end_fahrenheit:
    celsius = (fahrenheit - 32) * 5.0/9.0
    approx_celsius = (fahrenheit - 30)/2
    print(f"{fahrenheit}     {celsius:.2f}      {approx_celsius}")
    fahrenheit += step