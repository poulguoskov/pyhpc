import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('pi_timings.csv', delimiter=',')
procs = data[:, 0].astype(int)
times = data[:, 1]
speedup = times[0] / times

F = 0.97  # Try adjusting this
p_range = np.linspace(1, 12, 100)
amdahl = 1 / ((1 - F) + F / p_range)

plt.figure(figsize=(8, 5))
plt.plot(procs, speedup, 'o-', label='Measured')
plt.plot(p_range, amdahl, '--', label=f'Amdahl (F={F})')
plt.plot(procs, procs, ':', alpha=0.3, label='Ideal')
plt.xlabel('Number of processes')
plt.ylabel('Speedup')
plt.title('Pi Monte Carlo - Speedup with Amdahl fit')
plt.legend()
plt.grid(True)
plt.savefig('pi_speedup_amdahl.png', dpi=150, bbox_inches='tight')
print(f"F={F}, max theoretical speedup = {1/(1-F):.1f}")