## Using pasa to annotate gene
ref=""
trans="" ## trinity result or iso-seq full length rna
~/tools/PASApipeline-v2.5.1/Launch_PASA_pipeline.pl -c my.txt -C -R -g $ref  -t $trans --ALIGNERS  gmap,min
imap2 --CPU 16
