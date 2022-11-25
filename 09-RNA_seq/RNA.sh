kallisto index Ma.t2t.cds -i Ma
kallisto index Mi.t2t.cds -i Mi
kallisto index Mj.t2t.cds -i Mj
kallisto index Mp.t2t.cds -i Mp

for i in *R1.fq.gz
do
sbatch kallisto.slm $i Ma
done

for i in *R1.fq.gz
do
sbatch kallisto.slm $i Mi
done

for i in *R1.fq.gz
do
sbatch kallisto.slm $i Mj
done

for i in *R1.fq.gz
do
sbatch kallisto.slm $i Mp
done


### generate list file for all kallisto result

python filter_CV.py list earlyFemale | grep Ma_ > Ma.earlyFemale.exp
python filter_CV.py list J2 | grep Ma_ > Ma.J2.exp
python filter_CV.py list Femal | grep Ma_ > Ma.Female.exp
python filter_CV.py list Female | grep Ma_ > Ma.Female.exp
python filter_CV.py list J3J4 | grep Ma_ > Ma.J3J4.exp

## change Ma to other species. pass
##Using blastn result to remove 100% duplicated gene
### synlist = intact syntenic group
### synlist.rmdp = intact syntenic group (remove that contains 100% simliarty gene)

for i in *.exp
do; echo $i
python filter_step1.py XX.synlist.rmdp $i > XXX.info
done

### identify geneexpression pattern 
### for triploid 
### eg. Mp in J2,
python processTri.py Mp.J2.info info > Mp.J2.pattern
python processTri.py Mp.J2.info statis > Mp.J2.statis
### for tetraploid eg. Ma in J2:
python processTetra.py Ma.J2.info info > Ma.J2.pattern
python processTetra.py Ma.J2.info statis > Ma.J2.statis






