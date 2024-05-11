import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from convert_units import convert_units
from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_eos
from annotate_plot import annotate_plot
from generate_matrix import generate_matrix
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors


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
    plt.plot(fit_curve[:,0], fit_curve[:,1], color='black', label='Fit Curve')
    plt.xlabel('Volume ($\AA^3$/atom)')
    plt.ylabel('Energy (eV/atom)')
    plt.title(f"(Fit function name) Equation of State for {chemical_symbol} in DFT (Approximation Acronym)")
    plt.legend()

    # Annotate the graph
    plt.text(0.02, 0.95, chemical_symbol, transform=plt.gca().transAxes, fontsize=12)
    plt.text(0.5, 0.5, crystal_symmetry_symbol, transform=plt.gca().transAxes, fontsize=12, ha='center')
    plt.text(0.5, 0.55, "Bulk Modulus", transform=plt.gca().transAxes, fontsize=10, ha='center')
    plt.text(0.5, 0.6, "###.# GPa", transform=plt.gca().transAxes, fontsize=10, ha='center')
    plt.axvline(x=parameters['equilibrium_volume'], color='black', linestyle='--')
    plt.text(parameters['equilibrium_volume'], 0, f"{parameters['equilibrium_volume']:.2f} $\AA^3$/atom", rotation=90, ha='right', va='center')
    plt.text(0.02, 0.02, f"Created by (Your first name) (Your last name) ({datetime.datetime.now().isoformat()})", transform=plt.gca().transAxes, fontsize=8)

    if display:
        plt.show()
    else:
        plt.savefig(f"{chemical_symbol}_{crystal_symmetry_symbol}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")

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