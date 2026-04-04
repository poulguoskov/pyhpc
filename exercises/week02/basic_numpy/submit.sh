#!/bin/bash
#BSUB -J matpow
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -o batch_output/matpow_%J.out
#BSUB -e batch_output/matpow_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u matpow.py ./input.npy 10