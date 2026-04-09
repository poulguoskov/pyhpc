import numpy as np

def outer(x, y):
    return x[:, None] * y

x = np.array([1, 2])
y = np.array([3, 4, 5])
print(outer(x, y))
# Expected: [[3, 4, 5], [6, 8, 10]]