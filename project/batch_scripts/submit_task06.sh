#!/bin/bash
#BSUB -J task6_dynamic
#BSUB -q hpc
#BSUB -n 32
#BSUB -W 120
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -o batch_output/task6_dynamic_%J.out
#BSUB -e batch_output/task6_dynamic_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo "=== Dynamic scheduling speedup ==="
for n in 1 2 4 8 12 16 20 24 28 32; do
    python -u simulate_dynamic.py 100 $n subset100_ids.txt
done