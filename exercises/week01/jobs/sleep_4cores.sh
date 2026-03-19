#!/bin/bash              # This is a regular bash script
#BSUB -J 4cores         # Job name — shows up in bstat/bjobs
#BSUB -q hpc             # Queue — "hpc" is the default CPU queue
#BSUB -W 2               # Walltime limit — 5 minutes max
#BSUB -R "rusage[mem=512MB]"  # Memory per core — request 512MB
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -u s224193@dtu.dk
#BSUB -B
#BSUB -N
#BSUB -o sleeper_%J.out  # Where stdout goes (%J = job ID)
#BSUB -e sleeper_%J.err  # Where stderr goes

echo "CPU type: $CPUTYPEV"
/bin/sleep 60            # The actual command to run