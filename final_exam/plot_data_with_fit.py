import matplotlib.pyplot as plt
import numpy as np
__author__ = "Your Name"
def plot_data_with_fit(data, fit_curve, data_format='o', fit_format='-'):
    plt.figure()
    data_plot = plt.plot(data[0], data[1], data_format, label='Data Points')
    fit_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format, label='Fitted Curve')
    plt.legend()
    plt.title('Data Points and Fitted Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    return data_plot + fit_plot
if __name__ == "__main__":
    # Example data and fitted curve
    x_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([1, 4, 9, 16, 25])
    data = np.array([x_data, y_data])
    x_fit = np.linspace(0, 6, 100)
    y_fit = x_fit ** 2
    fit_curve = np.array([x_fit, y_fit])
    # Plot the data and fitted curve
    plot_data_with_fit(data, fit_curve)