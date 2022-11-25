import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

seqs=SeqIO.parse(sys.argv[1], "fasta")


dic = {}
for j in seqs:
    dic[str(j.id)] = str(j.seq).upper()

names = list(dic.keys())

dic1 = {} ## Mitgene to specific gene in MIG
for i in names:
    spc = i.split("[")[1].split("]")[0]
    gene = i.split("[")[0]
    dic1.setdefault(gene, []).append(i)
   
for j in dic1:  ## generate mergered fasta for each Mit gene
    filename = j + "merge.fasta"
    of = open(filename, "w")
    for i in dic1[j]:
        of.write(">" + i.split("[")[1].split("]")[0] + "\n")
        of.write(dic[i] + "\n")
    of.close()
    alnname = j + "merge.aln"
    os.system("mafft "+filename+" > "+alnname)
