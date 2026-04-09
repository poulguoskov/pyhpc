import numpy as np

def distmat_1d(x, y):
    return abs(x[:, None] - y)

x = np.array([1, 2])
y = np.array([3, 0.5, 1])
print(distmat_1d(x, y))
# Expected: [[2.0, 0.5, 0.0], [1.0, 1.5, 1.0]]