from os.path import join
import numpy as np
import matplotlib.pyplot as plt
from simulate import load_data, jacobi

LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'

with open('data/subset20_ids.txt', 'r') as f:
    building_ids = f.read().splitlines()

N = 4
ids = building_ids[:N]
MAX_ITER = 20_000
ABS_TOL = 1e-4

fig, axes = plt.subplots(1, N, figsize=(4*N, 4), constrained_layout=True)

for j, bid in enumerate(ids):
    u0, interior_mask = load_data(LOAD_DIR, bid)
    u = jacobi(u0, interior_mask, MAX_ITER, ABS_TOL)

    im = axes[j].imshow(u, cmap='hot', vmin=0, vmax=25)
    axes[j].set_title(f"ID: {bid}")

fig.colorbar(im, ax=axes, label='Temperature (°C)', shrink=0.8)
fig.suptitle("Task 3: Simulation Results", fontsize=14)
plt.savefig('plots/task3_results.png', dpi=150)
print("Saved plots/task3_results.png")