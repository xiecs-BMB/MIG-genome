##Initial annotation with BRAKER2

## mapping RNA-seq reads to genome using hisat2
## index
for i in *.fasta
do
hisat2-build $i ${i/.fasta/}
done
## mapping
for i in *R1.fastq.gz
do
hisat2 -x index -1 $i -2 ${i/R1.fastq.gz/R2.fastq.gz} -S ${i/R1.fastq.gz/sam} -p 6
samtools sort -@ 10 -o ${i/R1.fastq.gz/bam} ${i/R1.fastq.gz/sam}
done
## 
ls *.bam > list
sample=`python 1.py list`
echo $sample
ref=Mi.contig.fasta
spc=Mi_contig
braker.pl --gff3 --cores 48 --species=$spc --genome=$ref --bam=$sample
