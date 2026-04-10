import numpy as np
import matplotlib.pyplot as plt

procs = [1, 2, 4, 8, 12, 16, 20, 24, 28, 32]

static =  [1426.4177, 730.4167, 451.0799, 269.2841, 215.3476, 171.7654, 157.9478, 161.6810, 165.9068, 155.2348]
dynamic = [1409.9979, 719.2915, 378.4408, 233.3003, 186.6268, 154.3205, 148.4432, 150.2126, 151.1219, 151.7061]

speedup_s = [static[0] / t for t in static]
speedup_d = [dynamic[0] / t for t in dynamic]

F = 0.93
p_range = np.linspace(1, 32, 100)
amdahl = 1 / ((1 - F) + F / p_range)

plt.figure(figsize=(8, 5))
plt.plot(procs, speedup_s, 'o-', label='Static')
plt.plot(procs, speedup_d, 's-', label='Dynamic')
plt.plot(p_range, amdahl, '--', label=f'Amdahl (F={F})')
plt.plot(procs, procs, ':', alpha=0.3, label='Ideal')
plt.xlabel('Number of processes')
plt.ylabel('Speedup')
plt.title('Task 5 & 6: Static vs Dynamic Scheduling')
plt.legend()
plt.grid(True)
plt.savefig('plots/task56_speedup.png', dpi=150, bbox_inches='tight')
print("Saved plots/task56_speedup.png")