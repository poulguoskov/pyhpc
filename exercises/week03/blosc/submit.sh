#!/bin/bash
#BSUB -J blosc_random
#BSUB -q hpc
#BSUB -W 15
#BSUB -n 1
#BSUB -R "rusage[mem=8GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o batch_output/blosc_random_%J.out
#BSUB -e batch_output/blosc_random_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u blosc_timing.py 256
python -u blosc_timing.py 512
python -u blosc_timing.py 1024