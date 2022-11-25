## Using stingtie to annotate gene
ref=""
out=""
samtools merge -@ 20 merged.bam *.bam
stringtie -p 10 -o out.gtf merged.bam
perl ~/miniconda3/envs/RNA/opt/transdecoder/util/gtf_genome_to_cdna_fasta.pl out.gtf  $ref  > stringtie_tra
ns.fasta
perl ~/miniconda3/envs/RNA/opt/transdecoder/util/gtf_to_alignment_gff3.pl out.gtf > out.gff3
TransDecoder.LongOrfs -t stringtie_trans.fasta
TransDecoder.Predict -t stringtie_trans.fasta
~/miniconda3/envs/RNA/opt/transdecoder/util/cdna_alignment_orf_to_genome_orf.pl stringtie_trans.fasta.trans
decoder.gff3 out.gff3  stringtie_trans.fasta > $out
rm -rf string*
