### Using 3d-dna pipeline to construct scaffolds.
ref=$1

### merged_nodups.txt are generated from juicer.

awk -f ~/tools/3d-dna/utils/generate-assembly-file-from-fasta.awk $ref  > ${ref/.fasta/.ori.assembly}

~/tools/3d-dna/visualize/run-assembly-visualizer.sh  ${ref/.fasta/.ori.assembly} merged_nodups.txt

~/tools/3d-dna/run-asm-pipeline.sh -r 0 $ref merged_nodups.txt

## .FINAL.fasta .FINAL.assembly and .FINAL.hic are used to juicerbox.

## after juicerbox manually correct, a new assembly file are used to construct final scaffolds.

## Now we use 

~/tools/3d-dna/run-asm-pipeline-post-review.sh -r corrected.assembly merged_nodups.txt 
## The .FINAL.fasta is result file.
