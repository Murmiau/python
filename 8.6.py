import scipy
import scipy.linalg

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])

np.linalg.lstsq(A, B, rcond=None)

# Ответ:
[1.25,  0.5 , -0.25]
