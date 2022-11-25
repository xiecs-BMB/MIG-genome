from Bio import Phylo
from newick import loads
from io import StringIO
import sys
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-tree', type=str, default = None)
args = parser.parse_args()

def trees(tree):    
    Mg = ""
    list_ = []
    list_rm = []
    handle = StringIO(tree)
    tree = Phylo.read(handle,"newick")
    for i in range(len(tree.get_terminals())):
        if "Mg" in str(tree.get_terminals()[i]):
            Mg = tree.get_terminals()[i] 
        else:
            list_.append(str(tree.get_terminals()[i]))

    list_A=[]

    for i in list_:
        for j in list_:
            trace = str(tree.trace(i,j))
            count = trace.count("Clade")
            if count == 2:
                list_A.append(i)
    list_A = list(set(list_A))
    for x in list_:
        if x not in list_A:
            list_rm.append(x)
    return list_rm,list_
#########################################################
all_ = []
rm_ = []
detail = {}
gene = []
genes = {}
for i in open(args.tree,"r"):
    tmp = []
    tree = i.split("\n")[0]
    tmp,tmp1 = trees(tree)
    for j in tmp:
        all_.append(j.split("gene_")[0])
        genes.setdefault(j.split("gene_")[0], []).append(tmp1)
        gene.append(i.split("\n")[0])
        detail.setdefault(j, []).append(tree)
print(len(all_))
x = ""
y = 10000
for i in list(set(all_)):
    count = str(all_).count(str(i))
    print(i + "\t" + str(len(genes[i])) + "\t" + str(count/len(all_)))


