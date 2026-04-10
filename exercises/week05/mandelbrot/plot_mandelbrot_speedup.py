import numpy as np
import matplotlib.pyplot as plt

static = [10.9483, 7.5296, 7.4487, 6.5278, 5.7939, 4.9836, 4.7462, 4.1999, 4.0654, 3.7256, 3.2878, 3.2102]
chunked = [8.7237, 5.0297, 3.5073, 2.8124, 2.5745, 2.2601, 2.1888, 2.1291, 1.7778, 1.8870, 2.1027, 1.7975]

procs = np.arange(1, 13)
speedup_s = static[0] / np.array(static)
speedup_c = chunked[0] / np.array(chunked)

F = 0.91
p_range = np.linspace(1, 12, 100)
amdahl = 1 / ((1 - F) + F / p_range)

plt.figure(figsize=(8, 5))
plt.plot(procs, speedup_s, 'o-', label='Static')
plt.plot(procs, speedup_c, 's-', label='Chunked')
plt.plot(p_range, amdahl, '--', label=f'Amdahl (F={F})')
plt.plot(procs, procs, ':', alpha=0.3, label='Ideal')
plt.xlabel('Number of processes')
plt.ylabel('Speedup')
plt.title('Mandelbrot - Static vs Chunked Speedup')
plt.legend()
plt.grid(True)
plt.savefig('mandelbrot_speedup.png', dpi=150, bbox_inches='tight')
print("Saved mandelbrot_speedup.png")