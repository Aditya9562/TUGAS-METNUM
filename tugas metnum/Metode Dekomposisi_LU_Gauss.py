import numpy as np
import scipy.linalg as linalg

def solusi_persamaan_linear_lu_gauss(matriks_A, vektor_b):
    try:
        P, L, U = linalg.lu(matriks_A)
        y = linalg.solve_triangular(L, vektor_b, lower=True)
        x = linalg.solve_triangular(U, y)
        return x
    except ValueError:
        print("Matriks A singular. Tidak bisa melakukan dekomposisi LU.")
        return None

# Kode pengujian
A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([6, -4, 27])
x = solusi_persamaan_linear_lu_gauss(A, b)
print("Solusi menggunakan metode LU Gauss:", x)
