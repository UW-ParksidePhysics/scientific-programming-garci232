"""
Module for analyzing bivariate (x, y) data and calculating statistical properties.
"""
__author__ = "Nicolas Garcia"

import numpy as np
from scipy import stats
def calculate_bivariate_statistics(data):
    if data.shape[0] != 2:
        raise IndexError("Input data should have shape (2, M)")
    x_data, y_data = data
    mean_y = np.mean(y_data)
    std_dev_y = np.std(y_data)
    min_x = np.min(x_data)
    max_x = np.max(x_data)
    min_y = np.min(y_data)
    max_y = np.max(y_data)
    stats_desc = stats.describe(data, axis=1)
    return mean_y, std_dev_y, min_x, max_x, min_y, max_y, stats_desc
if __name__ == "__main__":
    # Example dataset creation
    x_values = np.linspace(-10, 10, 101)
    y_values = x_values ** 2
    data = np.array([x_values, y_values])
    # Calculate bivariate statistics
    mean_y, std_dev_y, min_x, max_x, min_y, max_y, stats_desc = calculate_bivariate_statistics(data)
    # Print the calculated statistics
    print(f"Mean of y: {mean_y}")
    print(f"Standard Deviation of y: {std_dev_y}")
    print(f"Minimum x-value: {min_x}")
    print(f"Maximum x-value: {max_x}")
    print(f"Minimum y-value: {min_y}")
    print(f"Maximum y-value: {max_y}")
    print(f"Stats description: {stats_desc}")