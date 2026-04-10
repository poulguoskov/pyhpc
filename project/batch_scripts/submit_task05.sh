#!/bin/bash
#BSUB -J task5_static
#BSUB -q hpc
#BSUB -n 32
#BSUB -W 120
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -o batch_output/task5_static_%J.out
#BSUB -e batch_output/task5_static_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo "=== Static scheduling speedup ==="
for n in 1 2 4 8 12 16 20 24 28 32; do
    python -u simulate_parallel.py 100 $n subset100_ids.txt
done