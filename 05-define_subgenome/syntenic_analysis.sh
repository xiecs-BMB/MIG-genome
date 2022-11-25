### Using jcvi,  MCScanX to perform syntenic analysi between polyploid species and Mg
#for each gff
i=""
gffread $i -g genome.fasta -x ${i/.gff/.cds} -y ${i/.gff/.pep}
#for each gff
i=$1
awk '{if($3=="mRNA") print $1"\t"$4"\t"$5"\t"substr($9,4,12)"\t"$6"\t"$7}' $i > ${i/.gff/.bed}
# diamond
diamond makedb --in Mg.pep -d db.dmnd

for i in *.pep
do
diamond blastp -q $i -d db.dmnd -e 1e-5 -f 6  -o ${i/.pep/.blast}
done

for i in *.bed
do
awk '{print $1,$4,$2,$3}' OFS="\t" $i > ${i/.bed/.gff}
~/tools/MCScanX/MCScanX ${i/.bed/}
done

## Using statis_collinearity.py to statis copy numpy 
for i in *.collinearity
do
python statis_collinearity.py $i > ${i/.collinearity/.count}
done
## Using Build_tree_from_syntenicgroup.py to build tree for those intact syntenic gene groups
collfile=""
python ~/MIG_code/05-define_subgenome/Build_tree_from_syntenicgroup.py all.pep all.pep $collfile

## Using count_top.py to statis topology, which are used to define A or B subgenome.
for i in {1..18}
do
cat Mg_${i}_*.tree > Chr${i}.tree 
python count_top.py -tree $i
done
## All subgenome info for assembly v1 are Subgenome_for_assembly_v1
