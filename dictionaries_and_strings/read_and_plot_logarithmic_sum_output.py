import matplotlib.pyplot as plt
def parse_sum_output(filename):
    tolerances = []
    errors = []
    maximum_indices = []

    with open(filename, 'r') as file:
        for line in file:
            if 'epsilon:' in line:
                parts = line.split(', ')
                epsilon = float(parts[0].split(': ')[1])
                exact_error = float(parts[1].split(': ')[1])
                n = int(parts[2].split('=')[1])
                tolerances.append(epsilon)
                errors.append(exact_error)
                maximum_indices.append(n)

    return tolerances, errors, maximum_indices
def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plt.figure()
    plt.semilogy(maximum_indices, tolerances, label='Tolerance')
    plt.semilogy(maximum_indices, errors, label='Approximation Error')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Value')
    plt.title('Logarithmic Sum Error Plot')
    plt.legend()
    plt.show()
# Usage
filename = 'logarithmic_sum.out'
tolerances, errors, maximum_indices = parse_sum_output(filename)
plot_logarithmic_sum_error(tolerances, errors, maximum_indices)