# 02613 Python & High-Performance Computing

Course repo for DTU course 02613 (Spring 2026).

## Structure

- `exercises/weekXX/` — Weekly exercises and job scripts
- `project/` — Mini-project (Wall Heating simulation)

## HPC Quick Reference

```bash
# SSH in
ssh <username>@login.hpc.dtu.dk
linuxsh

# Activate conda env
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Submit batch job
bsub < job.sh

# Check status
bstat
bjobs -p   # check why job is pending

# Kill job
bkill <JOBID>
```
