import sys


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
  """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
  return (5.0/9) * (fahrenheit_temperature - 32)
if __name__ == "__main__":
  fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
  celsius = convert_fahrenheit_to_celsius(fahrenheit)
  print(f"Temperature in Fahrenheit: {fahrenheit}°F")
  print(f"Temperature in Celsius: {celsius}°C")

