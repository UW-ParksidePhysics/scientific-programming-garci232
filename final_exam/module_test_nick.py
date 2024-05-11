"""
this code is a way to dynamically execute Python modules listed in modules by opening and executing their corresponding Python files.
"""
__author__ = "Nicolas Garcia"

modules = ['read_two_columns_text', 'calculate_bivariate_statistics', 'calculate_quadratic_fit', 'fit_curve_array', 'plot_data_with_fit', 'calculate_lowest_eigenvectors', 'annotate_plot']
for module in modules:
    with open(f'final_exam/{module}.py') as module_file:
        exec(module_file.read())