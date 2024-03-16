"""Demonstration of convert_temperature module usage:
Example Usage:
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> celsius_to_kelvin(0)
    273.15
    >>> kelvin_to_celsius(273.15)
    0.0
    >>> fahrenheit_to_kelvin(32)
    273.15
    >>> kelvin_to_fahrenheit(273.15)
    32.0
""" 
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
  
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
  
def celsius_to_kelvin(celsius):
    return celsius + 273.15
  
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
  
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
  
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
  
def test_conversion():
    assert celsius_to_fahrenheit(fahrenheit_to_celsius(32)) == 32
    assert kelvin_to_celsius(celsius_to_kelvin(0)) == 0
    assert kelvin_to_fahrenheit(fahrenheit_to_kelvin(32)) == 32
if __name__ == '__main__':
    import sys
  
    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <scale>")
        sys.exit(1)

    temperature = float(sys.argv[1])
    scale = sys.argv[2].lower()
    if scale == 'c':
      
        print(f"{celsius_to_fahrenheit(temperature)} F {celsius_to_kelvin(temperature)} K")
    elif scale == 'f':
        print(f"{fahrenheit_to_celsius(temperature)} C {fahrenheit_to_kelvin(temperature)} K")
    elif scale == 'k':
        print(f"{kelvin_to_celsius(temperature)} C {kelvin_to_fahrenheit(temperature)} F")
    else:
        print("Invalid scale provided. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")
