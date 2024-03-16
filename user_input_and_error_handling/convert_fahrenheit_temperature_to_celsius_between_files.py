import sys


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5.0/9
if __name__ == "__main__":
    try:
        with open('input_temperatures.txt', 'r') as file:
            lines = file.readlines()
        fahrenheit_degrees = []
        celsius_degrees = []
        for line in lines:
            if 'Fahrenheit degrees:' in line:
                fahrenheit = float(line.split(': ')[1].strip())
                celsius = convert_fahrenheit_to_celsius(fahrenheit)
                fahrenheit_degrees.append(fahrenheit)
                celsius_degrees.append(celsius)
        with open('output_temperatures.txt', 'w') as output_file:
            for f, c in zip(fahrenheit_degrees, celsius_degrees):
                output_file.write(f"Fahrenheit degrees: {f}  Celsius degrees: {c}\n")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
