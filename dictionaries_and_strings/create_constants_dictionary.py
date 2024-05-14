def constant_reader(file_name):
    # opening the file to be read
    data_file = open(file_name, 'r')
    # reading the data out of file
    data = data_file.readlines()
    # making an empty dictionary
    constants = dict()
    # scanning the file line by line starting from line 3 with index 2
    for i in range(2, len(data)):
        # loading the line ith data into line variable
        line = data[i]
        # finding the key of the constant which is name of the constant from first split to second last split of line
        key = ' '.join(line.strip().split()[0:-2])
        # finding the value which is the second last element in the split of a line so -2
        value = line.strip().split()[-2]
        # adding the key value pair in dictionary
        constants[key] = float(value)
    # returning the dictionary to main function
    return constants


def main():
    # file present in the current working directory
    file_name = "dictionaries_and_strings/constants.txt"
    # calling the constant_reader function to load the dictionary made in the constant variable
    constant = constant_reader(file_name)
    # Printing the whole dictionary
    for i in constant:
        print(str(i) + " :  " + str(constant[i]))


#calling the main function when we ran the program.
if __name__ == '__main__':
    main()