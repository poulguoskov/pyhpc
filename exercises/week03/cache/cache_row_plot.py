import numpy as np
import matplotlib.pyplot as plt

ns = np.array([100, 161, 259, 418, 672, 1083, 1743, 2807, 4520, 7279, 11721, 18874, 30392, 48939, 78805, 126896, 204336, 329034, 529832, 853168, 1373824, 2212216, 3562248, 5736153, 9236709, 14873521, 23950266, 38566204, 62101694, 100000000])

trows = [1.8436298705637455e-06, 1.8250592984259128e-06, 1.8762010180115699e-06, 1.8291990272700787e-06, 2.0612101070582866e-06, 2.2450601682066915e-06, 2.4099485017359256e-06, 2.7492712251842023e-06, 3.5946001298725606e-06, 4.063521046191454e-06, 5.768551491200924e-06, 7.549519650638103e-06, 9.85590973868966e-06, 1.766978995874524e-05, 5.158723099157214e-05, 9.862093953415752e-05, 0.00015642713056877256, 0.000270405279006809, 0.00047405548160895706, 0.0012968352786265314, 0.0022386979288421573, 0.0034331118897534905, 0.00496552926953882, 0.016129228570498526, 0.02421235561138019, 0.03897051775129512, 0.06327127696946264, 0.1015408542798832, 0.16495628172066062, 0.2619623383018188]

trows = np.array(trows)

# Size in KB (1D vector, float64)
size_kb = ns * 8 / 1024

# MFLOP/s: n multiplications per operation
mflops = ns / trows / 1e6

plt.figure(figsize=(10, 6))
plt.loglog(size_kb, mflops, 'o-', label='Row scaling')

for size, label in [(32, 'L1d 32KB'), (1024, 'L2 1MB'), (19712, 'L3 19.25MB')]:
    plt.axvline(x=size, color='gray', linestyle='--', alpha=0.5)
    plt.text(size * 1.1, max(mflops) * 0.5, label, rotation=90, va='center', fontsize=8)

plt.xlabel('Row vector size (KB)')
plt.ylabel('MFLOP/s')
plt.title('Row Vector Scaling Performance (Xeon Gold 6126)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('cache_row_performance.png', dpi=150, bbox_inches='tight')
print("Saved cache_row_performance.png")