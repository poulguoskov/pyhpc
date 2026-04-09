import numpy as np
from time import perf_counter as time

def distance_matrix_loop(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)
    cos_p1 = np.cos(p1[:, 0])
    cos_p2 = np.cos(p2[:, 0])
    D = np.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        dsin2 = np.sin(0.5 * (p1[i] - p2)) ** 2
        a = dsin2[:, 0] + cos_p1[i] * cos_p2 * dsin2[:, 1]
        D[i, :] = 2 * np.arcsin(np.sqrt(a))
    D *= 6371
    return D

def distance_matrix_noloop(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)
    dsin2 = np.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cos_p1 = np.cos(p1[:, 0])
    cos_p2 = np.cos(p2[:, 0])
    a = dsin2[:, :, 0] + cos_p1[:, None] * cos_p2[None, :] * dsin2[:, :, 1]
    D = 6371 * 2 * np.arcsin(np.sqrt(a))
    return D

loop_times = []
noloop_times = []
ns = np.logspace(1, 4, 30).astype(int)
n_repeat = 5

for n in ns:
    p1 = np.random.rand(n, 2) * 180 - 90
    p2 = np.random.rand(n, 2) * 180 - 90

    t = time()
    for _ in range(n_repeat):
        distance_matrix_loop(p1, p2)
    loop_times.append((time() - t) / n_repeat)

    t = time()
    for _ in range(n_repeat):
        distance_matrix_noloop(p1, p2)
    noloop_times.append((time() - t) / n_repeat)

print('ns =', list(ns))
print('loop_times =', loop_times)
print('noloop_times =', noloop_times)