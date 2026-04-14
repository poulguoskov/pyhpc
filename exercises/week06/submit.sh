#!/bin/bash
#BSUB -J reduction_bench
#BSUB -q hpc
#BSUB -n 32
#BSUB -W 60
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -R "rusage[mem=8GB]"
#BSUB -o batch_output/reduction_bench_%J.out
#BSUB -e batch_output/reduction_bench_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

DATA=/dtu/projects/02613_2025/data/celeba/celeba_100K.npy

echo "=== Chunk size tuning (8 processes) ==="
for c in 2 4 8 16 32 64 128; do
    python -u reduction.py $DATA 8 $
done

echo "=== Speedup (chunk=64) ==="
for n in 1 2 4 8 12 16 20 24 28 32; do
    python -u reduction.py $DATA $n 64
done