from os.path import join
import sys
import time

import numpy as np
from multiprocessing import Pool


def load_data(load_dir, bid):
    SIZE = 512
    u = np.zeros((SIZE + 2, SIZE + 2))
    u[1:-1, 1:-1] = np.load(join(load_dir, f"{bid}_domain.npy"))
    interior_mask = np.load(join(load_dir, f"{bid}_interior.npy"))
    return u, interior_mask


def jacobi(u, interior_mask, max_iter, atol=1e-6):
    u = np.copy(u)

    for i in range(max_iter):
        # Compute average of left, right, up and down neighbors, see eq. (1)
        u_new = 0.25 * (u[1:-1, :-2] + u[1:-1, 2:] + u[:-2, 1:-1] + u[2:, 1:-1])
        u_new_interior = u_new[interior_mask]
        delta = np.abs(u[1:-1, 1:-1][interior_mask] - u_new_interior).max()
        u[1:-1, 1:-1][interior_mask] = u_new_interior

        if delta < atol:
            break
    return u


def summary_stats(u, interior_mask):
    u_interior = u[1:-1, 1:-1][interior_mask]
    mean_temp = u_interior.mean()
    std_temp = u_interior.std()
    pct_above_18 = np.sum(u_interior > 18) / u_interior.size * 100
    pct_below_15 = np.sum(u_interior < 15) / u_interior.size * 100
    return {
        'mean_temp': mean_temp,
        'std_temp': std_temp,
        'pct_above_18': pct_above_18,
        'pct_below_15': pct_below_15,
    }


# Module-level constants (needed for multiprocessing pickling)
LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
MAX_ITER = 20_000
ABS_TOL = 1e-4


def process_building(bid):
    u0, interior_mask = load_data(LOAD_DIR, bid)
    u = jacobi(u0, interior_mask, MAX_ITER, ABS_TOL)
    stats = summary_stats(u, interior_mask)
    return bid, stats


if __name__ == '__main__':
    if len(sys.argv) < 2:
        N = 1
    else:
        N = int(sys.argv[1])

    n_proc = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    if len(sys.argv) >= 4:
        ids_file = join('data/', sys.argv[3])
    else:
        ids_file = join(LOAD_DIR, 'building_ids.txt')

    with open(ids_file, 'r') as f:
        building_ids = [line.strip() for line in f if line.strip()]

    building_ids = building_ids[:N]
    N = len(building_ids)

    # Dynamic scheduling: small chunks
    chunk_size = 1

    start = time.time()
    with Pool(n_proc) as pool:
        results = pool.map(process_building, building_ids, chunksize=chunk_size)

    elapsed = time.time() - start
    print(f"{n_proc},{elapsed:.4f}")

    # Print summary statistics in CSV format
    stat_keys = ['mean_temp', 'std_temp', 'pct_above_18', 'pct_below_15']
    print('building_id, ' + ', '.join(stat_keys))  # CSV header
    for bid, stats in results:
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))