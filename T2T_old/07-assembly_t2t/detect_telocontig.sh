#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=normal
#SBATCH -J 'te'
#SBATCH --ntasks-per-node=20
#SBATCH --time=120:00:00

fa=$1
RepeatMasker -pa 20   -lib Telomere.seq  -no_is -nolow -gff $fa
