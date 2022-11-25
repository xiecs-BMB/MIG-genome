#!/bin/sh
#SBATCH -J MitoZ
#SBATCH -c 30
#SBATCH -p normal

R1=""
R2=""
prefix=$1

singularity exec --bind /beegfs/ ~/opt/singularity-image/MitoZ_v3.4.sif \
mitoz all  \
--workdir mitoz_$prefix \
--outprefix $prefix \
--thread_number 30 \
--clade Nematoda \
--fq1 $R1 \
--fq2 $R2 \
--data_size_for_mt_assembly 0 \
--assembler megahit \
--kmers_megahit 59 79 99 119 141 \
--memory 50 \
--requiring_taxa Nematoda
