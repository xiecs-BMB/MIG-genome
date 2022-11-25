##Using EVM to  integrate all evidence to obtain a final gene structure information.
#genome.fasta = genome file
#gene.gff3 = Ab initio file from BRAKER2 and Stringtie
#pasa.gff3 = RNA-seq evidence from PASA

~/tools/EVidenceModeler-1.1.1/EvmUtils/partition_EVM_inputs.pl  --genome genome.fasta  --gene_predictions gene.gff3 --transcript_alignments pasa.gff3 --segmentSize 100000 --overlapSize 10000 --partition_listing partitions_list.out

~/tools/EVidenceModeler-1.1.1/EvmUtils/write_EVM_commands.pl --genome genome.fasta  --weights `pwd`/wei.txt --gene_predictions gene.gff3  --transcript_alignments pasa.gff3  --output_file_name evm_test.out --partitions partitions_list.out > commands.list

parallel -j 50 < commands.list

~/tools/EVidenceModeler-1.1.1/EvmUtils/recombine_EVM_partial_outputs.pl --partitions partitions_list.out --output_file_name evm_test.out

../EVidenceModeler-1.1.1/EvmUtils/convert_EVM_outputs_to_GFF3.pl  --partitions partitions_list.out --outpu
 evm_test.out  --genome genome.fasta

find . -regex \".*evm_test.out.gff3\" -exec cat {} \; > EVM.final.gff3

## EVM.final.gff3 file are further formated to generate final gff file.


