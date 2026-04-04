import sys
import numpy as np

v = np.array([float(x) for x in sys.argv[1:]])
print(np.sqrt(np.sum(v**2)))