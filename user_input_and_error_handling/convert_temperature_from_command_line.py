import sys


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
    return (5.0/9) * (fahrenheit_temperature - 32)
if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Fahrenheit temperature missing on the command line.")

        fahrenheit = float(sys.argv[1])
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"Temperature in Fahrenheit: {fahrenheit}°F")
        print(f"Temperature in Celsius: {celsius}°C")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

Rerun

