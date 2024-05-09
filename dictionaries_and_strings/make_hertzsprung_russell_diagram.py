import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Constants
astronomical_unit = 1.495978707e11  # meters


def star_colormap(star_b_minus_vs):
    # Create color map from B-V = -0.33 (#7070ff) to 1.40 (#ff7f7f)
    # yellow = #ffff7f at B-V = 0.81
    number_of_gradient_points = 256
    white_index = int((0.33 / (0.33 + 1.40)) * number_of_gradient_points)
    yellow_index = int(((0.81 + .33) / (0.33 + 1.40)) * number_of_gradient_points)

    color_values = np.ones((number_of_gradient_points, 4))
    # Red values
    color_values[:white_index, 0] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 0] = np.linspace(255 / 255, 255 / 255, yellow_index - white_index)
    color_values[yellow_index:, 0] = np.linspace(255 / 255, 255 / 255, number_of_gradient_points - yellow_index)
    # Green values
    color_values[:white_index, 1] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 1] = np.linspace(255 / 255, 255 / 255, yellow_index - white_index)
    color_values[yellow_index:, 1] = np.linspace(255 / 255, 127 / 255, number_of_gradient_points - yellow_index)
    # Blue values
    color_values[:white_index, 2] = np.linspace(255 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 2] = np.linspace(255 / 255, 127 / 255, yellow_index - white_index)
    color_values[yellow_index:, 2] = np.linspace(127 / 255, 127 / 255, number_of_gradient_points - yellow_index)

    new_colormap = ListedColormap(color_values)
    scaled_b_minus_vs = (star_b_minus_vs - np.amin(star_b_minus_vs)) / (
            np.amax(star_b_minus_vs) - np.amin(star_b_minus_vs))

    return scaled_b_minus_vs, new_colormap


def parallax_to_distance(parallax):
    """Take parallax in milliarcseconds and convert to distance in meters"""
    parallax_in_radians = np.radians(parallax / 3600000)
    distance = astronomical_unit / np.tan(parallax_in_radians)
    return distance


def apparent_to_absolute_magnitude(apparent_magnitude, distance):
    """Calculate absolute magnitude from apparent magnitude and distance in meters"""
    distance_in_parsecs = distance / (astronomical_unit / (648000 / np.pi))
    absolute_magnitude = apparent_magnitude - 5 * np.log10(distance_in_parsecs) + 5
    return absolute_magnitude


def read_file(filename):
    """Read four column data from HIPPARCOS satellite and return a nested dictionary"""
    hipparcos_data = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            hipparcos_data[data[0]] = {
                'parallax': float(data[1]),
                'apparent_magnitude': float(data[2]),
                'blue_minus_visual': float(data[3])
            }
    return hipparcos_data


if __name__ == '__main__':
    # Apply read function to the data file and produce a nested dictionary
    hipparcos_dictionary = read_file('hipparcos_data.txt')

    star_absolute_magnitudes = []
    star_b_minus_vs = []

    for star_data in hipparcos_dictionary.values():
        distance = parallax_to_distance(star_data['parallax'])
        absolute_magnitude = apparent_to_absolute_magnitude(star_data['apparent_magnitude'], distance)
        star_absolute_magnitudes.append(absolute_magnitude)
        star_b_minus_vs.append(star_data['blue_minus_visual'])

    star_absolute_magnitudes = np.array(star_absolute_magnitudes)
    star_b_minus_vs = np.array(star_b_minus_vs)

    plt.style.use('dark_background')
    star_absolute_magnitudes = np.negative(star_absolute_magnitudes)
    scaled_b_minus_v, hr_diagram_colormap = star_colormap(star_b_minus_vs)

    plt.xlabel('B-V')
    plt.ylabel('Absolute Magnitude')

    plt.xlim(-0.5, 2.0)
    plt.ylim(20, -10)

    plt.gca().invert_yaxis()
    plt.gca().invert_xaxis()

    plt.scatter(star_b_minus_vs, star_absolute_magnitudes, c=scaled_b_minus_v, cmap=hr_diagram_colormap, s=20)

    # Labels for brightest stars and the Sun
    brightest_star_names = ['Sirius', 'Canopus', 'Alpha Centauri A', 'Alpha Centauri B', 'Arcturus']
    brightest_star_bv = [-0.03, 0.15, 0.71, 0.71, 1.23]
    brightest_star_abs_mag = [-1.46, -0.72, 4.38, 5.71, -0.30]

    for i, name in enumerate(brightest_star_names):
        plt.text(brightest_star_bv[i], brightest_star_abs_mag[i], name, fontsize=8, ha='right')

    # Luminosity scale
    plt.text(-0.45, 10, 'Luminosity ↓', fontsize=10, rotation=90, va='center', ha='center')

    # Color bar
    cbar = plt.colorbar()
    cbar.set_label('Temperature (K)', rotation=270, labelpad=15)

    # Spectral class axis
    plt.text(-0.5, 15, 'O', fontsize=8, ha='center')
    plt.text(2.0, 15, 'M', fontsize=8, ha='center')

    # Title
    plt.title('Hertzsprung-Russell Diagram')

    # Credits
    plt.text(-0.5, 20, 'Created by Your Names', fontsize=8)

    plt.show()
