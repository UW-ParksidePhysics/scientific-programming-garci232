import numpy as np
__author__ = "Your Name"
def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    if square_matrix.shape[0] != square_matrix.shape[1]:
        raise ValueError("Input matrix must be square")
    if number_of_eigenvectors > square_matrix.shape[0]:
        raise ValueError("Number of eigenvectors exceeds matrix dimensions")
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    sorted_indices = np.argsort(eigenvalues)
    smallest_indices = sorted_indices[:number_of_eigenvectors]
    sorted_eigenvalues = eigenvalues[smallest_indices]
    sorted_eigenvectors = eigenvectors[:, smallest_indices]
    return sorted_eigenvalues, sorted_eigenvectors
if __name__ == "__main__":
    # Test with a specified matrix and number of eigenvectors
    matrix = np.array([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
    num_eigenvectors = 2
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix, num_eigenvectors)
    # Print the calculated eigenvalues and eigenvectors
    print("Eigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)