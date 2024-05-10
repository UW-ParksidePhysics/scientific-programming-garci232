"""
 this code provides a reusable module for fitting a quadratic polynomial to a set of x-y data and demonstrates its usage with an example dataset.
"""
__author__ = "Garcia, Nicolas"

import numpy as np
def calculate_quadratic_fit(data):
    """
    Fits a quadratic polynomial to provided x-y data and returns the coefficients,
    rounding small coefficients (below a given threshold) to zero.

    Parameters:
    data (ndarray): A numpy ndarray with shape (2, M), where 2 represents x-y data and M is the number of data points.

    Returns:
    ndarray: An array of shape (3) containing the polynomial coefficients: [constant, linear, quadratic].

    Raises:
    IndexError: If the input data array has inappropriate dimensions.
    """
    if data.shape[0] != 2:
        raise IndexError("Input data should have shape (2, M)")
    x_data, y_data = data
    coefficients = np.polyfit(x_data, y_data, 2)
    # Round small coefficients to zero
    threshold = 1e-10
    coefficients = np.where(np.abs(coefficients) < threshold, 0, coefficients)
    return coefficients

if __name__ == "__main__":
    # Generate test data
    x_values = np.linspace(-1, 1, 100)
    y_values = x_values ** 2
    data = np.array([x_values, y_values])
    # Calculate quadratic fit
    quadratic_coefficients = calculate_quadratic_fit(data)
    # Print the calculated coefficients
    print("Quadratic Coefficients:")
    print(quadratic_coefficients)