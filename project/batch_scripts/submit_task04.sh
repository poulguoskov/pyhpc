#!/bin/bash
#BSUB -J task4_profile
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 10
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o batch_output/task4_profile_%J.out
#BSUB -e batch_output/task4_profile_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

kernprof -l simulate.py 1
python -m line_profiler -rmt simulate.py.lprof