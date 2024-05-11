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
    data = [
        (465135987493600034e+01, -3.909045511666799939e+03),
        (487223095732699996e+01, -3.909086625209999966e+03),
        (487334642985200084e+01, -3.909086820315700152e+03),
        (532287442761199969e+01, -3.909156118321399845e+03),
        (602279843114600055e+01, -3.909231727055099782e+03),
        (700352187811899896e+01, -3.909286760309400051e+03),
        (798963267898399891e+01, -3.909233127352899828e+03),
        (862862182672799989e+01, -3.909156889900199985e+03)
    ]

    converted_data = []
    for volume, energy in data:
        converted_volume = convert_units(volume, 'cubic_bohr_per_atom', 'cubic_angstroms_per_atom')
        converted_energy = convert_units(energy, 'rydberg_per_atom', 'electron_volts_per_atom')
        converted_data.append((converted_volume, converted_energy))

    for volume, energy in converted_data:
        print(f"Volume: {volume:.2f} cubic angstroms/atom, Energy: {energy:.2f} eV/atom")
