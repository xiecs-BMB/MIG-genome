import sys
import os
import math
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import multiprocessing

pro = SeqIO.parse(sys.argv[1], "fasta") ## Read protein
cds = SeqIO.parse(sys.argv[2], "fasta") ## Read cds

dic_cds = {}
dic_pro = {}

for i in cds:
    dic_cds[i.id]=str(i.seq)

for i in pro:
    dic_pro[i.id]=str(i.seq)

##read_bed
gene2chr = {}
for i in open("All.bed","r"):
    a = i.strip().split("\t")
    gene2chr[a[3]] = a[0]

def check_scaffolds(list_in):
    tmp1=[]
    for j in list_in :
        tmp1 += [gene2chr[j]] 
    if len(list(set(tmp1))) ==  len(list_in):
        tmp1 = tmp1
    else:
        tmp1 = []
    return tmp1

def read_coll(x):
    dic_tmp = {}
    list_tmp = []
    for i in open(x,"r"):
        if i[0] != "#":
            gene = i.split(":")[-1].strip().split("\t")
            if gene[0][0:2]  == "Mg":
                Mg = gene[0]
                other = gene[1]
            else:
                Mg = gene[1]
                other = gene[0]
            dic_tmp.setdefault(Mg, []).append(other)
    for i in dic_tmp:
        tmp1 = check_scaffolds(dic_tmp[i])
        if len(tmp1) != 0 : 
            if len(dic_tmp[i]) == 3 :## 4 for tetraploid, 3 for triplod 
                dic_tmp[i] += [i]
                list_tmp += [dic_tmp[i]]      
    return list_tmp


inlist=read_coll(sys.argv[3])

def write_and_mafft(list_in):
    for i in list_in:
        filename = i[-1]+".fasta" #  Mgname.
        of = open(filename, "w") 
        for j in i[0:-1]: # genes except Mg.
            print(j)
            of.write(">" + gene2chr[j] +"\n" + dic_pro[j] + "\n") ## convert gene name to chrname 
        of.close()

        alnname = filename.replace(".fasta",".aln")
        os.system("mafft "+filename +" > "+ alnname)
        os.system("Gblocks "+ alnname + " -t=p -b4=5 -b5=h")
        os.system("iqtree -s "+alnname+"-gb")       
        rmlist = [i[-1]+".aln", i[-1]+".fasta", i[-1]+".aln-gb", i[-1]+".aln-gb.bionj", i[-1]+".aln-gb.ckp.gz", i[-1]+".aln-gb.htm", i[-1]+".aln-gb.iqtree", i[-1]+".aln-gb.log", i[-1]+".aln-gb.mldist", i[-1]+".aln-gb.model.gz"]
        os.system("rm " + " ".join(rmlist))
        nn = gene2chr[i[-1]] + "_"+i[-1]+".tree"
        os.system("mv "+ i[-1]+".aln-gb.treefile "+nn)

#write_and_mafft(inlist)

if __name__ == '__main__':
    list_run=[]
    list_all=read_coll(sys.argv[3])
    list_test=list_all[0:20]
    m = 20 ## CPU
    n = int(math.ceil(len(list_all) / float(m)))
    pool = multiprocessing.Pool(processes=m)
    for i in range(0, len(list_test), n):
        list_run.append(list_test[i: i+n])
    pool.map(write_and_mafft,list_run)
    pool.close()
    pool.join()

