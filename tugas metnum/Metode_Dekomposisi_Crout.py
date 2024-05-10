import numpy as np
import scipy.linalg as linalg

def solusi_persamaan_linear_crout(matriks_A, vektor_b):
    try:
        P, L, U = linalg.lu(matriks_A, permute_l=False)
        y = linalg.solve_triangular(L, vektor_b, lower=True)
        x = linalg.solve_triangular(U, y)
        return x
    except ValueError:
        print("Matriks A singular. Tidak bisa melakukan dekomposisi LU.")
        return None

# Kode pengujian
A = np.array([[2, 1], [1, -1]])
b = np.array([4, 1])
x = solusi_persamaan_linear_crout(A, b)
print("Solusi menggunakan metode Crout:", x)
