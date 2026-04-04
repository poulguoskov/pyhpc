import sys
import numpy as np
from time import perf_counter

A = np.load(sys.argv[1])
p = int(sys.argv[2])

start = perf_counter()
result = A.copy()
for _ in range(p):
    result = result @ A
elapsed = perf_counter() - start

np.save('result.npy', result)
print(elapsed)