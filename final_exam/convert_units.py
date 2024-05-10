def convert_units(value, from_units, to_units):
  conversions = {
    ('cubic_bohr_per_atom', 'cubic_angstroms_per_atom'): 0.14818471147216278,
          ('rydberg_per_atom', 'electron_volts_per_atom'): 13.605693122994,
          ('rydberg_per_cubic_bohr', 'gigapascals'): 14710.507848260711
      }
  conversion_key = (from_units, to_units)
  if conversion_key in conversions:
      conversion_factor = conversions[conversion_key]
      return value * conversion_factor
  else:
      raise ValueError(f"Unsupported conversion from {from_units} to {to_units}")
if __name__ == "__main__":
  # Test cases
  value_1 = 1.0
  from_units_1 = 'cubic_bohr_per_atom'
  to_units_1 = 'cubic_angstroms_per_atom'
  print(f"{value_1} {from_units_1} is equal to {convert_units(value_1, from_units_1, to_units_1)} {to_units_1}")
  value_2 = 2.0
  from_units_2 = 'rydberg_per_atom'
  to_units_2 = 'electron_volts_per_atom'
  print(f"{value_2} {from_units_2} is equal to {convert_units(value_2, from_units_2, to_units_2)} {to_units_2}")
  value_3 = 3.0
  from_units_3 = 'rydberg_per_atom'
  to_units_3 = 'gigapascals'
  print(f"{value_3} {from_units_3} is equal to {convert_units(value_3, from_units_3, to_units_3)} {to_units_3}")