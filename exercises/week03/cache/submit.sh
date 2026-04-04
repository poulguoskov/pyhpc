#!/bin/bash
#BSUB -J cache_row_plot
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=1GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o batch_output/cache_row_plot_%J.out
#BSUB -e batch_output/cache_row_plot_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u cache_row_plot.py