import sys
import numpy as np

diag = np.array([float(x) for x in sys.argv[1:]])
matrix = np.diag(diag)
np.save('matrix.npy', matrix)
print(matrix)