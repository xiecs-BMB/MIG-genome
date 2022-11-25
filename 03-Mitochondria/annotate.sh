#!/bin/sh
#SBATCH -J MitoZ
#SBATCH -c 8
#SBATCH -p normal

R1=""
R2=""
ref=""
prefix=""

singularity exec --bind /beegfs/ ~/opt/singularity-image/MitoZ_v3.4.sif \
mitoz annotate  \
--workdir mitoz \
--outprefix $prefix \
--thread_number 8 \
--clade Nematoda \
--species_name "Meloidogyne incognita" \
--fq1 $R1 \
--fq2 $R2 \
--fastafiles $ref
