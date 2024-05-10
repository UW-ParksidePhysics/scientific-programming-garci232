import os
import numpy as np
import matplotlib.pyplot as plt
import datetime
from final_exam import convert_units
from final_exam import read_two_columns_text
from final_exam import calculate_bivariate_statistics
from final_exam import calculate_quadratic_fit
from final_exam import fit_eos
from final_exam import annotate_plot
from final_exam import generate_matrix
from final_exam import calculate_lowest_eigenvectors
def parse_file_name(filename):
    """
    Extracts metadata from the filename.
    Parameters:
    filename (str): The filename containing metadata.
    Returns:
    tuple: (chemical_symbol, crystal_symmetry_symbol, density_functional_acronym)
    """
    parts = filename.split('.')
    return parts[0], parts[1], parts[2]
def plot_data_and_fit(data, fit_curve, parameters, chemical_symbol, crystal_symmetry_symbol, display=True):
    """
    Plots data points, fit curve, and annotates the plot.
    Parameters:
    data (numpy.ndarray): Array of data points.
    fit_curve (numpy.ndarray): Array of fit curve points.
    parameters (dict): Dictionary of parameters.
    chemical_symbol (str): Chemical symbol.
    crystal_symmetry_symbol (str): Crystal symmetry symbol.
    display (bool): Flag to display the plot (default=True).
    """
    plt.figure()
    plt.scatter(data[:,0], data[:,1], label='Data Points')
    plt.plot(fit_curve[:,0], fit_curve[:,1], color='red', label='Fit Curve')
    plt.xlabel('Volume')
    plt.ylabel('Energy')
    plt.title(f"{chemical_symbol} - {crystal_symmetry_symbol}")
    plt.legend()
    if display:
        plt.show()
    else:
        now = datetime.datetime.now()
        plt.savefig(f"{chemical_symbol}_{crystal_symmetry_symbol}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png")
def fit_an_equation_of_state(filename):
    """
    Processes the file containing volumes and energies, calculates statistics, quadratic coefficients, and fits an equation of state.
    Then, it plots the data and the fit curve.
    Parameters:
    filename (str): Path to the file containing volumes and energies.
    """
    data = read_two_columns_text(filename)
    stats = calculate_bivariate_statistics(data)
    quad_coeffs = calculate_quadratic_fit(data)
    fit_curve = fit_eos(data, quad_coeffs)
    chemical_symbol, crystal_symmetry_symbol, _ = parse_file_name(os.path.basename(filename))

    plot_data_and_fit(data, fit_curve, stats, chemical_symbol, crystal_symmetry_symbol)
def visualize_vectors_in_space():
    """
    Generates a spatial grid and matrix, calculates eigenvectors and eigenvalues, and plots the results.
    """
    matrix = generate_matrix()
    eigenvectors, eigenvalues = calculate_lowest_eigenvectors(matrix)
    # Plot eigenvectors and eigenvalues
if __name__ == "__main__":
    # Test visualize_vectors_in_space function
    visualize_vectors_in_space()
    # Fit an equation of state using the provided data file
    fit_an_equation_of_state("final_exam/volumes_energies.dat")