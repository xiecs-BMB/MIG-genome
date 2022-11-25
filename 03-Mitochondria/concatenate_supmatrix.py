## python concatenate_supmatrix.py >  supmetrix.fasta
import sys
import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#
files = os.listdir("./")
filelist = []
for i in files:
    if "merge.aln" in i :
        filelist.append(i)
#
dic = {}
spc = []
for i in filelist:
    seqs = SeqIO.parse(i, "fasta")
    for j in seqs:
        spc.append(str(j.id))
#
spc = list(set(spc))    

dic_merge = {}

for i in filelist: ## For gene 
    seqs = SeqIO.parse(i, "fasta")
    tmp = {}
    for j in seqs: ## Read gene
        tmp[j.id] = str(j.seq)
    for j in spc: ## For gene
        if j not in tmp.keys():
            dic_merge.setdefault(j, []).append("-"*len(list(tmp.values())[0]))
        else:
            dic_merge.setdefault(j, []).append(tmp[j])

for j in dic_merge:
    print(">" + j)
    print("".join(dic_merge[j]))
    
