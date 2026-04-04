from time import perf_counter as time
import numpy as np

ns = np.round(np.logspace(2, 8, 30)).astype(int)
n_repeat = 100
trows = []

for n in ns:
    mat = np.random.rand(1, n)

    trow = time()
    for _ in range(n_repeat):
        mat[0, :] * 2
    trow = time() - trow

    trows.append(trow / n_repeat)

print(f"ns = {list(ns)}")
print(f"trows = {trows}")