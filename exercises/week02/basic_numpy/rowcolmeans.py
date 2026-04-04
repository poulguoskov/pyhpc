import sys
import numpy as np

matrix = np.load(sys.argv[1])
np.save('cols.npy', matrix.mean(axis=0))
np.save('rows.npy', matrix.mean(axis=1))
print('cols:', matrix.mean(axis=0))
print('rows:', matrix.mean(axis=1))