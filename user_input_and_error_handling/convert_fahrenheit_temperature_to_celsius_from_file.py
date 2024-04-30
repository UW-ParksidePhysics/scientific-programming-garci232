import sys


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
  """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
  return (5.0/9) * (fahrenheit_temperature - 32)
if __name__ == "__main__":
  try:
      with open('temperature_data.txt', 'r') as file:
          content = file.readlines()
          fahrenheit = float(content[3].split()[2])
          celsius = convert_fahrenheit_to_celsius(fahrenheit)
          print(f"Temperature in Fahrenheit: {fahrenheit}°F")
          print(f"Temperature in Celsius: {celsius}°C")
  except FileNotFoundError:
      print("File not found.")
  except Exception as e:
      print(f"An error occurred: {e}")

