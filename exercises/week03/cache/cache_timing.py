from time import perf_counter as time
import numpy as np

SIZE = 100
n_repeat = 1000

mat = np.random.rand(SIZE, SIZE)

# Time row scaling
trow = time()
for _ in range(n_repeat):
    2 * mat[0, :]
trow = time() - trow

# Time column scaling
tcol = time()
for _ in range(n_repeat):
    2 * mat[:, 0]
tcol = time() - tcol

print(f"Row avg: {trow / n_repeat:.10f} sec")
print(f"Col avg: {tcol / n_repeat:.10f} sec")
print(f"Ratio (col/row): {tcol / trow:.2f}x")