from os.path import join
import numpy as np
import matplotlib.pyplot as plt

LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'

# Load building IDs
with open('data/subset20_ids.txt', 'r') as f:
    building_ids = f.read().splitlines()

# Pick first 4 buildings to visualize
N = 4
ids = building_ids[:N]

fig, axes = plt.subplots(2, N, figsize=(4*N, 8), constrained_layout=True)

for j, bid in enumerate(ids):
    domain = np.load(join(LOAD_DIR, f"{bid}_domain.npy"))
    interior = np.load(join(LOAD_DIR, f"{bid}_interior.npy"))

    # Top row: domain (initial conditions)
    im = axes[0, j].imshow(domain, cmap='hot', vmin=0, vmax=25)
    axes[0, j].set_title(f"ID: {bid}")
    if j == 0:
        axes[0, j].set_ylabel("Domain (u₀)")

    # Bottom row: interior mask
    axes[1, j].imshow(interior, cmap='gray')
    if j == 0:
        axes[1, j].set_ylabel("Interior mask")

fig.colorbar(im, ax=axes[0, :], label='Temperature (°C)', shrink=0.8)
fig.suptitle("Task 1: Input Data Visualization", fontsize=14)
plt.savefig('plots/task1_input_data.png', dpi=150)
print("Saved plots/task1_input_data.png")