#Create a dictionary of data
viscosity_data = '''air,120,291.15,18.27
nitrogen,111,300.55,17.81
oxygen,127,292.25,20.18
carbon dioxide,240,293.15,14.8
carbon monoxide,118,288.15,17.2
hydrogen,72,293.85,8.76
ammonia,370,293.15,9.82
sulphur dioxide,416,293.65,12.54'''

mu_data = {} #Create empty list

# Split the data into lines
lines = viscosity_data.split('\n')

# Process each line and populate mu_data
for line in lines:
    gas_name, C, T_0, mu_0 = line.split(',') #split the line by comma
    mu_data[gas_name] = {'C': float(C), 'T_0': float(T_0), 'mu_0': float(mu_0)}

# Test the data in dictionary
print("mu_data['air']['C'] == 120.0 : "+ str(mu_data['air']['C'] == 120.0))
print("mu_data['hydrogen']['T_0'] == 293.85 : "+str(mu_data['hydrogen']['T_0'] == 293.85))
print("mu_data['sulphur dioxide']['mu_0'] == 12.54 : "+str(mu_data['sulphur dioxide']['mu_0'] == 12.54))