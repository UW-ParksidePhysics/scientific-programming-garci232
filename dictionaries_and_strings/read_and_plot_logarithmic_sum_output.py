import numpy as np
import matplotlib.pyplot as plt

def parse_sum_output(filename):
    tolerances = []
    errors = []
    maximum_indices = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("epsilon:"):
                parts = line.split(", ")
                tolerance = float(parts[0].split(": ")[1])
                error = float(parts[1].split(": ")[1])
                n = int(parts[2].split("=")[1])
                tolerances.append(tolerance)
                errors.append(error)
                maximum_indices.append(n)

    return tolerances, errors, maximum_indices

def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plt.figure()
    plt.semilogy(maximum_indices, tolerances, label='Tolerance')
    plt.semilogy(maximum_indices, errors, label='Approximation Error')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Logarithmic Scale')
    plt.title('Tolerance and Approximation Error vs Maximum Index')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filename = "dictionaries_and_strings/logarithmic_sum.py"
    tolerances, errors, maximum_indices = parse_sum_output(filename)
    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)