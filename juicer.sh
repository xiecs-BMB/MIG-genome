#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=normal
#SBATCH -J 'juicer'
#SBATCH --ntasks-per-node=10

mkdir reference 
mkdir fastq ### mv fastq file of Hi-C data into fastq

ref=$1

ln -s $ref reference/assembly.fasta

bwa index reference/assembly.fasta

python ~/tools/jucier/juicer/misc/generate_site_positions.py \
MboI reference/genome_MboI.txt reference/assembly.fasta

python ~/scrit/get_len.py reference/assembly.fasta > reference/genome.size

~/tools/jucier/juicer/scripts/juicer.sh \
-g genome \
-s MboI \
-z reference/assembly.fasta \
-y reference/genome_MboI.txt \
-p reference/genome.size \
-D ~/duantong/tools/jucier/juicer \
-t 72

