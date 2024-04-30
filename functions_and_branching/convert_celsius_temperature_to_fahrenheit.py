<<<<<<< HEAD
def convert_celsius_to_fahrenheit(celsius_temperature):
  """Convert input temperature in degrees Celsius to degrees Fahrenheit."""
  return (9.0/5) * celsius_temperature + 32
  
def convert_fahrenheit_to_celsius(fahrenheit_temperature):
  """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
  return (5.0/9) * (fahrenheit_temperature - 32)
  
if __name__ == "__main__":
  celsius_temperatures = [0, 21, 100]
  print('T_C\tT-c(T_F(T_C))')
  for some_celsius_temperature in celsius_temperatures:
      converted_temperature = convert_fahrenheit_to_celsius(convert_celsius_to_fahrenheit(some_celsius_temperature))
      print(f'{some_celsius_temperature}\t\t{converted_temperature}')
  
=======
def convert_celsius_to_fahrenheit(celsius_temperature):
  """Convert input temperature in degrees Celsius to degrees Fahrenheit."""
  return (9.0/5) * celsius_temperature + 32
  
def convert_fahrenheit_to_celsius(fahrenheit_temperature):
  """Convert input temperature in degrees Fahrenheit to degrees Celsius."""
  return (5.0/9) * (fahrenheit_temperature - 32)
  
if __name__ == "__main__":
  celsius_temperatures = [0, 21, 100]
  print('T_C\tT-c(T_F(T_C))')
  for some_celsius_temperature in celsius_temperatures:
      converted_temperature = convert_fahrenheit_to_celsius(convert_celsius_to_fahrenheit(some_celsius_temperature))
      print(f'{some_celsius_temperature}\t\t{converted_temperature}')
  
>>>>>>> 5f713a787ed925c152b5f599b14e9a664ce1fe9f
