## count syntenic copy number
import sys
dic = {}
for i in open(sys.argv[1],"r"):
    if i[0]! = "#":
        gene = i.split(":")[-1].strip().split("\t")
        if gene[0][0:2]  == "Mg":
            Mg = gene[0]
            other = gene[1]
        else:
            Mg = gene[1]
            other = gene[0]
        dic.setdefault(Mg, []).append(other)

for j in dic:
    print(j + "\t" + str(len(dic[j])))
     
