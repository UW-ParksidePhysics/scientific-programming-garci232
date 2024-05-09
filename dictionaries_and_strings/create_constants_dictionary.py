def parse_constants_file(file_path):
              constants = {}
              with open(file_path, 'r') as file:
                  for line in file:
                      if line.strip():
                          key, value = line.strip().split(':')
                          constants[key.strip()] = float(value.strip())
              return constants
          # Specify the path to the constants.txt file
file_path = 'constants.txt'
          # Call the parse_constants_file function to parse the file and store the constants in a dictionary
constants = parse_constants_file(file_path)
          # Print the dictionary of constants
print(constants)