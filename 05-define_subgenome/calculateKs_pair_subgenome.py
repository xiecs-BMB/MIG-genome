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
    dic_cds[i.id]=i.seq

for i in pro:
    dic_pro[i.id]=i.seq

def read_coll(x):
    list_ = []
    for i in open(x,"r"):
        if i[0] != "#":
            gene = i.split(":")[-1].strip().split("\t")
            name = gene[0]+"_vs_"+gene[1]
            list_.append(name)
    return list_

Kaks_calculator_Path="/beegfs/home/xcs/tools/KaKs_Calculator2.0/bin/Linux/KaKs_Calculator"

def write_and_mafft(list_in):
    for name in list_in:
        cds_name = name+".cds"
        pro_name = name+".pep"
        aln_name = name+".aln"
        code_name = name+".code"
        axt_name = name+".axt"  
        kaks_name = name+".kaks"
        file_cds = open(cds_name,"w")
        gene = name.split("_vs_")
        file_cds.write(">" + gene[0] + "\n" + str(dic_cds[gene[0]]) + "\n" + ">" + gene[1] + "\n" + str(dic_cds[gene[1]]) + "\n")
        file_cds.close()
        file_pro = open(pro_name,"w")
        file_pro.write(">" + gene[0] + "\n" + str(dic_pro[gene[0]]) + "\n" + ">" + gene[1] + "\n" + str(dic_pro[gene[1]]) + "\n")
        file_pro.close()
        os.system("muscle  -in "+pro_name +" -out "+aln_name)
        os.system("pal2nal.pl "+aln_name+" "+cds_name+" -output fasta> "+code_name)
        os.system("python ~/script/Fast2AXT.py "+code_name +" > "+axt_name)
        os.system(Kaks_calculator_Path + " -i "+axt_name+" -o "+kaks_name+" -m YN")
        os.system("rm "+pro_name+" "+aln_name+" "+cds_name+" "+code_name+" "+axt_name)

if __name__ == '__main__':
    list_run=[]
    list_all=read_coll(sys.argv[3])
    list_test=list_all[0:20] ## remove this index
    m = 20 ## CPU
    n = int(math.ceil(len(list_all) / float(m)))
    pool = multiprocessing.Pool(processes=m)
    for i in range(0, len(list_test), n):
        list_run.append(list_test[i: i+n])
    pool.map(write_and_mafft,list_run)
    pool.close()
    pool.join()
