import numpy as np

def magnitude(v):
    return np.sqrt(np.sum(v**2))

print(magnitude(np.array([1, 1, 3, 3, 4])))