#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=dell
#SBATCH -J 'bp'
#SBATCH --ntasks-per-node=10
#SBATCH --time=120:00:00

i=$1
j=$2

blastp -db $i -num_threads 10 -max_target_seqs 1 -query  $j  -evalue 0.001 -outfmt 6 -out ${j/.pep/}vs${i/.pep/.tab}
blastp -db $j -num_threads 10 -max_target_seqs 1 -query  $i  -evalue 0.001 -outfmt 6 -out ${i/.pep/}vs${j/.pep/}.tab

python  get_rbh.py ${j/.pep/}vs${i/.pep/.tab} ${i/.pep/}vs${i/.pep/.tab}  > ${j/.pep/}vs${i/.pep/}.rbh
