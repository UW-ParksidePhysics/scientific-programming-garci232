import numpy as np
import matplotlib.pyplot as plt
# Create the matrix H
matrix_dimension = 5
s = 1 / (2 * (1 / (matrix_dimension + 1))**2)
values = np.array([2 - 1000, -12 - 100, -12 - 10, -12 - 1, -12])
H = s * np.diagflat(values)
# Find the eigenvalues and eigenvectors of H
eigenvalues, eigenvectors = np.linalg.eig(H)
# Set x_values for plotting the fifth eigenvector
x_values = np.linspace(1 / (matrix_dimension + 1), matrix_dimension / (matrix_dimension + 1), matrix_dimension)
fifth_eigenvector = eigenvectors[:, 4]
# Define the range for the sin function plot
x_range = np.linspace(0, 1, 1000)
sin_function = np.sqrt(2) * np.sin(np.pi * x_range)
# Plot the fifth eigenvector and sin function
plt.figure(figsize=(10, 6))
plt.plot(x_values, fifth_eigenvector, label='Fifth Eigenvector', marker='o')
plt.plot(x_range, sin_function, label=r'$\sqrt{2} \sin(\pi x)$', linestyle='--')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fifth Eigenvector and Sin Function for 5x5 Matrix')
plt.grid(True)
plt.show()