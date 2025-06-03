

import numpy as np
# X = np.array([[1, 2, 3],
#               [4, 5, 6], 
#               [7,8,9]])

# print(X)

# det_X = np.linalg.det(X)
# print(det_X)


# Résoudre Ax = b
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 13])
x = np.linalg.solve(A, b)

print(x)
