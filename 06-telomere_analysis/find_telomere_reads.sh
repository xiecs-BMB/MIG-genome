#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=normal
#SBATCH -J 'telomere_repeat'
#SBATCH --ntasks-per-node=10
#SBATCH --time=120:00:00

i=$1

bwa mem -t 10 -o ${i/1.fastq.gz/.sam} telomere_repeat.fasta  $i ${i/1.fastq.gz/2.fastq.gz}

samtools view -b -F 4 ${i/1.fastq.gz/.sam} > ${i/1.fastq.gz/.bam}

samtools view ${i/1.fastq.gz/.bam} |grep 150M| wc -l 
