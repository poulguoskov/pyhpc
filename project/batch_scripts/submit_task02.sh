#!/bin/bash
#BSUB -J task2_time
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 120
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o batch_output/task2_time_%J.out
#BSUB -e batch_output/task2_time_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

time python -u simulate.py 100 subset100_ids.txt