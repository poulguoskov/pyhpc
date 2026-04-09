#!/bin/bash
#BSUB -J task1_viz
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 2
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o batch_output/task1_viz_%J.out
#BSUB -e batch_output/task1_viz_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u visualize_input.py