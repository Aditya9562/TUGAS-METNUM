import numpy as np

def solve_linear_eq_inv(matrix_A, vector_b):
    try:
        inv_A = np.linalg.inv(matrix_A)
        x = np.dot(inv_A, vector_b)
        return x
    except np.linalg.LinAlgError:
        print("Matrix A is singular. Cannot compute inverse.")
        return None

# Testing code
A = np.array([[3, 2, 1], [1, -1, 2], [2, 3, 1]])
b = np.array([9, 8, 3])
x = solve_linear_eq_inv(A, b)
print("Solution using inverse matrix method:", x)
