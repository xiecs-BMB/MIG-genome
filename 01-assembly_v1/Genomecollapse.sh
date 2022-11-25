##Check for collapse of scaffolds from homologous chromosomes.
##If scaffolds are collapsed, the normalized depth are twice that of in whole genome.

ref=$1
R1=$2
R2=$3
bwa index $ref

python ~/script/get_len.py  $ref > ${ref/.fasta/.len}

bedtools makewindows -g ${ref/.fasta/.len} -w 100000 > ${ref/.fasta/.100k.windows}

bwa mem -t 20 $ref -o ${ref/.fasta/.sam} $R1 $R2

samtools sort -@ 10 -o ${ref/.fasta/.bam} ${ref/.fasta/.sam}

bedtools coverage -sorted -a ${ref/.fasta/.100k.windows} -b ${ref/.fasta/.bam} > ${ref/.fasta/.cov}

##Using a custom py script to calculate normalized depth.

python ~/script/normal.py  ${ref/.fasta/.cov} >  ${ref/.fasta/.nor}
