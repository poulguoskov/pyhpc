#!/bin/bash
#BSUB -J evenfilter
#BSUB -q hpc
#BSUB -W 5
#BSUB -R "rusage[mem=512MB]"
#BSUB -o batch_output/evenfilter_%J.out
#BSUB -e batch_output/evenfilter_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python -u evenfilter.py 0 1 4 2 3 -2