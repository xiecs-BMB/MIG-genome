#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=Normal
#SBATCH -J 'Nextpolish'
#SBATCH --ntasks-per-node=30
#SBATCH --time=120:00:00

cfg=$1 # short reads, long reads and reference are set in cfg file

/beegfs/home/xcs/tools/NextPolish/nextPolish $cfg


