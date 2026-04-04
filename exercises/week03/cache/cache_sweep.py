from time import perf_counter as time
import numpy as np

ns = np.round(np.logspace(1, 4.5, 30)).astype(int)
n_repeat = 1000

trows = []
tcols = []

for n in ns:
    mat = np.random.rand(n, n)

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

    trows.append(trow / n_repeat)
    tcols.append(tcol / n_repeat)

print(f"dtype: {mat.dtype}")
print(f"ns = {list(ns)}")
print(f"trows = {trows}")
print(f"tcols = {tcols}")