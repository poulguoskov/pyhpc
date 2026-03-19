#!/bin/bash              # This is a regular bash script
#BSUB -J sleeper         # Job name — shows up in bstat/bjobs
#BSUB -q hpc             # Queue — "hpc" is the default CPU queue
#BSUB -W 5               # Walltime limit — 5 minutes max
#BSUB -R "rusage[mem=512MB]"  # Memory per core — request 512MB
#BSUB -o sleeper_%J.out  # Where stdout goes (%J = job ID)
#BSUB -e sleeper_%J.err  # Where stderr goes

/bin/sleep 60            # The actual command to run