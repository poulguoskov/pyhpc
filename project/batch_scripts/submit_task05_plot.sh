#!/bin/bash
#BSUB -J task5_plot
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 2
#BSUB -R "rusage[mem=2GB]"
#BSUB -o batch_output/task5_plot_%J.out
#BSUB -e batch_output/task5_plot_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u plot_task5.py