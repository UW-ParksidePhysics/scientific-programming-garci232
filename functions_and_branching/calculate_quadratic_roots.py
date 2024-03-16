import numpy as np
def calculate_quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real roots
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return float(root1), float(root2)
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return float(root)
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = np.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
# Test cases with known solutions
def test_single_root():
    a, b, c = 1, 2, 1
    expected_roots = -1.0
    calculated_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 2x + 1 = 0: x = {expected_roots} ; calculate_quadratic_roots({a}, {b}, {c}) = {calculated_roots}")

def test_roots_float():
    a, b, c = 1, -2, -3
    expected_roots = (3.0, -1.0)
    calculated_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 - 2x - 3 = 0: x = {expected_roots} ; calculate_quadratic_roots({a}, {b}, {c}) = {calculated_roots}")
def test_roots_complex():
    a, b, c = 2, 2, -1
    expected_roots = (1j, -1j)
    calculated_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 0x + 1 = 0: x = {expected_roots} ; calculate_quadratic_roots({a}, {b}, {c}) = {calculated_roots}")
# Run the test cases
test_single_root()
test_roots_float()
test_roots_complex()