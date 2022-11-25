## Using EDTA.pl to annotate TE

for i in *scaffolds.fasta
do
EDTA.pl -t 30 --genome $i
done

for i in *_scaffolds.fasta
do
nohup srun -J test -p smp -c 10 RepeatMasker -pa 10 -gff -a -lib  ${i}.mod.EDTA.TElib.fa  $i &
done
## Maskered genome are used to annotate
