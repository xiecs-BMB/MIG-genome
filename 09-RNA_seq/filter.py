import sys

x = 0
dic = {}
for i in open(sys.argv[1]): ## read checked list
    a = i.strip().split("\t")
    x = x+1
    name = "Homo_"+str(x)    
    dic[name] = a[0:3]

exp = {}
for i in open(sys.argv[2]): ## read exp list
    a = i.strip().split(" ")  
    exp[a[0]] = a[1]

subinfo = {}
for i in open("MIGtoSub","r"): ## bedtools intersect -f 0.5 -a MIG.bed -b seqTo0.bed -wb > MIGtoSub
    a = i.strip().split("\t")
    subinfo[a[3]] = a[-2]

for j in dic.keys():
    glist = dic[j]
    a = 0
    elist = []
    sublist = []
    for i in glist:
        if i in exp.keys():
            a = a+1
            elist.append(exp[i])
            sublist.append(subinfo[i])
    if a == 3 : ## all of gene are CV >30%
        explist=list(map(float, elist))
        if sum(explist) >= 5: ## TPM sum > 5
            print(j + "\t" + "\t".join(dic[j]) + "\t" + "\t".join(elist) + "\t" +"\t".join(sublist))
        print("Count_exp")
