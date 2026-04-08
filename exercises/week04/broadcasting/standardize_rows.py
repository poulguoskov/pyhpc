import numpy as np

def standardize_rows(data, mean, std):
    return (data - mean) / std

# Test with the example from the exercise
data = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
mean = np.array([0.5, 1, 3], dtype=float)
std = np.array([1, 2, 3], dtype=float)

result = standardize_rows(data, mean, std)
print(result)
# Expected: [[0.5, 0.5, 0.0], [3.5, 2.0, 1.0]]