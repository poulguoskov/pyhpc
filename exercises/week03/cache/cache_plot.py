import numpy as np
import matplotlib.pyplot as plt

ns = np.array([10, 13, 17, 23, 30, 40, 53, 70, 92, 122, 161, 213, 281, 371, 489, 646, 853, 1126, 1487, 1964, 2593, 3424, 4520, 5968, 7880, 10405, 13738, 18139, 23950, 31623])

trows = [1.7391128931194544e-06, 1.751065021380782e-06, 1.7406200058758259e-06, 1.7123240977525712e-06, 1.7038118094205856e-06, 1.7357259057462216e-06, 1.7745720688253642e-06, 1.7406819388270377e-06, 1.7516519874334334e-06, 1.7583691515028477e-06, 1.8527670763432979e-06, 1.860158983618021e-06, 1.8383660353720188e-06, 1.8982989713549613e-06, 1.9144839607179166e-06, 2.0374758169054985e-06, 2.158595947548747e-06, 2.2867901716381312e-06, 2.440395997837186e-06, 2.676469972357154e-06, 2.9232660308480264e-06, 3.210094990208745e-06, 3.5919910296797753e-06, 4.15105395950377e-06, 4.843558883294463e-06, 5.766859976574778e-06, 7.011539069935679e-06, 8.651884039863944e-06, 1.0759120807051659e-05, 1.3585767010226846e-05]

tcols = [1.7034909687936306e-06, 1.7336390446871519e-06, 1.7243609763681888e-06, 1.7472119070589542e-06, 1.7428640276193618e-06, 1.7775879241526126e-06, 1.7640050500631333e-06, 1.8039830029010772e-06, 1.8022090662270785e-06, 1.8547039944678545e-06, 1.985040958970785e-06, 2.05528293736279e-06, 2.1739429794251917e-06, 2.3252968676388265e-06, 2.485956996679306e-06, 2.7764951810240746e-06, 2.831128193065524e-06, 3.0648838728666303e-06, 3.371394006535411e-06, 3.75772500410676e-06, 4.296967992559075e-06, 6.804343080148101e-06, 6.1813229694962506e-06, 7.83595908433199e-06, 9.413881925866008e-06, 1.4449252979829908e-05, 2.0315660862252117e-05, 4.4597851810976863e-05, 8.725713100284337e-05, 0.00011787821515463293]

trows = np.array(trows)
tcols = np.array(tcols)

# Matrix size in KB (n x n float64)
size_kb = ns**2 * 8 / 1024

# MFLOP/s: each operation is n FLOPs
mflops_row = ns / trows / 1e6
mflops_col = ns / tcols / 1e6

plt.figure(figsize=(10, 6))
plt.loglog(size_kb, mflops_row, 'o-', label='Row scaling')
plt.loglog(size_kb, mflops_col, 's-', label='Column scaling')

# Mark cache boundaries (Xeon Gold 6126)
for size, label in [(32, 'L1d 32KB'), (1024, 'L2 1MB'), (19712, 'L3 19.25MB')]:
    plt.axvline(x=size, color='gray', linestyle='--', alpha=0.5)
    plt.text(size, plt.ylim()[1]*0.5, label, rotation=90, va='center', fontsize=8)

plt.xlabel('Matrix size (KB)')
plt.ylabel('MFLOP/s')
plt.title('Row vs Column Scaling Performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('cache_performance.png', dpi=150, bbox_inches='tight')
print("Saved cache_performance.png")

plt.figure(figsize=(10, 6))
plt.semilogx(size_kb, mflops_row / mflops_col, 'o-')
plt.xlabel('Matrix size (KB)')
plt.ylabel('MFLOP/s ratio (row / col)')
plt.title('Row vs Column Performance Ratio')
for size, label in [(32, 'L1d 32KB'), (1024, 'L2 1MB'), (19712, 'L3 19.25MB')]:
    plt.axvline(x=size, color='gray', linestyle='--', alpha=0.5)
    plt.text(size, 1.5, label, rotation=90, va='center', fontsize=8)
plt.grid(True, alpha=0.3)
plt.savefig('cache_ratio.png', dpi=150, bbox_inches='tight')
print("Saved cache_ratio.png")