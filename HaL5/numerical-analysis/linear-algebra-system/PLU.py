import scipy.linalg as la
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
b = np.array([7, 18, 7])
P, L, U = la.lu(A)
# x = la.solve_triangular(L, la.solve(U, b))

print(P)
print(L)
print(U)
# print(x)