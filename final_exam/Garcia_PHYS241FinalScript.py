import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
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
    Extract metadata from the formatted filename.

    Args:
        filename (str): The file path to parse.

    Returns:
        tuple: Containing three strings (chemical_symbol, crystal_symmetry_symbol,
               density_functional_acronym).
    """
    file_name = os.path.basename(filename)
    parts = file_name.split('.')
    if len(parts) < 4:
        raise ValueError("Filename does not contain enough parts to extract the necessary information.")

    return parts[0], parts[1], parts[2]

def plot_data_and_fit(data, fit_curve, title, xlabel, ylabel, save_fig=False):
    """
    Plots data points and fit curve, annotates the plot, and displays or saves the figure.

    Args:
        data (numpy array): Numpy array containing data points.
        fit_curve (numpy array): Numpy array containing the fit curve.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        save_fig (bool): If True, save the figure; otherwise, display it.
    """
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], label='Data Points')
    plt.plot(data[:, 0], fit_curve, color='red', label='Fit Curve')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    if save_fig:
        now = datetime.datetime.now()
        plt.savefig(f"{title}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png")
    else:
        plt.show()

def fit_an_equation_of_state(filename):
    """
    Process the file and plot results related to equation of state fits.

    Args:
        filename (str): Path to the data file.
    """
    chemical_symbol, crystal_symmetry_symbol, density_functional_acronym = parse_file_name(filename)
    print(f"Processed file for: {chemical_symbol} in {crystal_symmetry_symbol} structure using {density_functional_acronym} approximation.")

    try:
        data = read_two_columns_text(filename)
    except OSError as e:
        print(e)
        return

    volumes = data[0]
    energies = data[1]
    statistics = calculate_bivariate_statistics(data)
    print(f"Statistics:\nMean of Y: {statistics[0]}\nStandard Deviation of Y: {statistics[1]}\nMin X: {statistics[2]}, Max X: {statistics[3]}\nMin Y: {statistics[4]}, Max Y: {statistics[5]}")

    quadratic_coefficients = calculate_quadratic_fit(data)
    print(f"Quadratic Coefficients: {quadratic_coefficients}")

    eos_fit_curve, eos_parameters = fit_eos(volumes, energies, quadratic_coefficients, eos='murnaghan', number_of_points=120)
    print(f"EOS Fit Curve: {eos_fit_curve}")
    print(f"EOS Parameters: {eos_parameters}")

    plot_data_and_fit(data, eos_fit_curve, f"Murnaghan Equation of State for {chemical_symbol} in DFT {crystal_symmetry_symbol}",
                      r'$V$ ($\mathit{\AA}^3$/atom)', r'$E$ (eV/atom)', display_graph=True)

def visualize_vectors_in_space():
    """
    Generate spatial grid, calculate eigenvectors and eigenvalues, and plot the results.
    """
    pass

if __name__ == "__main__":
    # Test cases
    visualize_vectors_in_space()
    fit_an_equation_of_state("final_exam/volumes_energies.dat")