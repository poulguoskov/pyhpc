import sys
import numpy as np

def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)

    dsin2 = np.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cos_p1 = np.cos(p1[:, 0])
    cos_p2 = np.cos(p2[:, 0])
    a = dsin2[:, :, 0] + cos_p1[:, None] * cos_p2[None, :] * dsin2[:, :, 1]
    D = 6371 * 2 * np.arcsin(np.sqrt(a))

    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)