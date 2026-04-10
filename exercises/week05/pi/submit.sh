#!/bin/bash
#BSUB -J pi_map
#BSUB -q hpc
#BSUB -n 10
#BSUB -W 5
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -o batch_output/pi_map_%J.out
#BSUB -e batch_output/pi_map_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo "=== pool.map version ==="
time python -u pi_map.py 10