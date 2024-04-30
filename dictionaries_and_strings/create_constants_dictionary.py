def parse_constants_file(filename):
  constants = {}
  with open(filename, 'r') as file:
      for line in file:
          parts = line.strip().split(':')
          name = parts[0].strip()
          value = float(parts[1].strip().split()[0])
          constants[name] = value
  return constants

if __name__ == '__main__':
  constants = parse_constants_file('constants.txt')
  test_values = {
      'speed of light': 299792458,
      'gravitational constant': 6.67430e-11,
      'Planck constant': 6.62607015e-34,
      'electron mass': 9.10938356e-31,
      'proton mass': 1.6726219e-27,
      'Avogadro constant': 6.02214076e23,
      'Boltzmann constant': 1.380649e-23
  }

  for constant, expected_value in test_values.items():
      if constant in constants:
          actual_value = constants[constant]
          print(f"{constant}: {actual_value} {'matches' if actual_value == expected_value else 'does not match'} the expected value")
      else:
          print(f"{constant} not found in the constants dictionary")