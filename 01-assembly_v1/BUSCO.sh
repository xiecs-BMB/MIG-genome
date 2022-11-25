#!/bin/sh
#SBATCH -J BUSCO5
#SBATCH -c 30
#SBATCH -p normal

db=/beegfs/home/bdx/DATA/busco_database/nematoda_odb10
fa=$1 ## protein file 
cores=30
singularity exec --bind /beegfs /beegfs/home/bdx/opt/singularity-image/busco-5.4.3.sif \
busco --in $fa -l $db -f -m protein  --out ${fa/.fa/_dir} -c $cores --long --offline
