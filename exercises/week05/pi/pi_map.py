import random
import multiprocessing
import sys

def sample(_):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    samples = 1000000
    n_proc = int(sys.argv[1])
    chunk_size = samples // n_proc
    pool = multiprocessing.Pool(n_proc)
    res = pool.map(sample, range(samples), chunksize=chunk_size)
    hits = sum(res)
    pi = 4.0 * hits / samples
    print(pi)