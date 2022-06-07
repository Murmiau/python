import scipy
import scipy.linalg

A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)
P, L, U

# Составим вектор B, приняв значения переменных X0 = X1 = X2 = 1
# B = [10, 5, 24]
import numpy as np
B = np.array([10, 5, 24])
np.linalg.solve(A, B)

# array([12.375 , -1.5625,  0.25  ])
