import numpy as np
__author__ = "Nicolas Garcia"
def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):
    if maximum_x < minimum_x:
        raise ArithmeticError("Maximum x should be greater than minimum x")
    if number_of_points <= 2:
        raise IndexError("Number of points should be greater than 2")
    x_values = np.linspace(minimum_x, maximum_x, number_of_points)
    y_values = np.polyval(quadratic_coefficients, x_values)
    fit_curve = np.vstack((x_values, y_values))
    return fit_curve
if __name__ == "__main__":
    # Test with a quadratic equation y = x^2
    quadratic_coefficients = [0, 0, 1]  # [constant, linear, quadratic]
    minimum_x = -10
    maximum_x = 10
    number_of_points = 100
    fit_curve = fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points)
    # Print the fit curve and its shape
    print(f"Fit Curve:\n{fit_curve}")
    print(f"Fit Curve Shape: {fit_curve.shape}")