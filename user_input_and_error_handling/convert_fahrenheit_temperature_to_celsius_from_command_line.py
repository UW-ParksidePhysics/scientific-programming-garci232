import sys


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
    return (5.0/9) * (fahrenheit_temperature - 32)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_fahrenheit_temperature_to_celsius_from_command_line.py <fahrenheit_temperature>")
        sys.exit(1)
    fahrenheit = float(sys.argv[1])
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"Temperature in Fahrenheit: {fahrenheit}°F")
    print(f"Temperature in Celsius: {celsius}°C")
  
