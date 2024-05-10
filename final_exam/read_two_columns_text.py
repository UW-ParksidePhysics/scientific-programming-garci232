"""
 this script runs standalone tests from various modules to verify their functionality. It provides a way to automate testing for multiple modules at once.
"""
__author__ = "Nicolas Garcia"

import numpy as np
def read_two_columns_text(filename):
    try:
        data = np.loadtxt(filename).T
        return data
    except OSError as e:
        raise OSError(f"Error reading file: {filename}") from e

if __name__ == "__main__":
    filename = 'final_exam/volumes_energies.dat'
    data = read_two_columns_text(filename)
    print(f'{data=}, shape={data.shape}')