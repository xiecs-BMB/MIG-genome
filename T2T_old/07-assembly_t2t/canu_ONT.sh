i=$1 ## WHF4-1.nanopore.fastq
dir=${i/.nanopore.fastq/_canu}
pre=${i/.nanopore.fastq/}
canu -p $pre -d $dir genomeSize=210m useGrid=false maxThreads=100 maxMemory=300g corOutCoverage=200 "batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50"  -raw -nanopore  $i
