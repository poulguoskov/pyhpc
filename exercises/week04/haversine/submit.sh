#!/bin/bash
#BSUB -J bench
#BSUB -q hpc
#BSUB -W 15
#BSUB -n 1
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o batch_output/bench_%J.out
#BSUB -e batch_output/bench_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python benchmark.py