import sys


dic={}
for i in open("list"): ## list of kallisto 
    print(i)
    a=i.strip().split("_out")[0].split("WHF4-1")[1]
    dic.setdefault(a, []).append(i.strip())


for j in dic.keys():
    if len(dic[j]) == 3:
        print(j)
        print(dic[j])
    elif len(dic[j]) == 2:
        print(j)
        print(dic[j])


stage=sys.argv[2]

dic2={}

if stage in dic.keys():
    
    for i in dic[stage]:        

        with open(i) as f:
            lines = f.readlines()
            for gene in lines[1:]:
                gene = gene.strip().split("\t")
                dic2.setdefault(gene[0], []).append(float(gene[-1]))
import numpy as np 


def coeffvar(data):
    mean = np.mean(data)
    std = np.std(data,ddof=0)
    cv = std/mean
    return cv

if len(list(dic2.keys())) >= 100:

    for j in dic2.keys():
        if coeffvar(dic2[j]) <= 0.3:
            print(j, np.mean(dic2[j]))


        
