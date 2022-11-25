#!/bin/sh
#SBATCH -J get_mito
#SBATCH -c 60
#SBATCH -p normal

$Reads1=""
$Reads2=""

get_organelle_from_reads.py \
	-1 $Reads1\
	-2 $Reads2 \
	-s /beegfs/home/bdx/DATA/ref_genome/Mg_Mito/Mg_mito.fasta \
	--reduce-reads-for-coverage inf --max-reads inf \
	--disentangle-time-limit 72000 \
	-F animal_mt -t 60 -o get_organelle -R 15 -k 21,45,65,85,105,115,127
