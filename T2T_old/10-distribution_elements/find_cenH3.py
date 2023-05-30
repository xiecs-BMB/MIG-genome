import sys
y = ""
##

a = "TCGGGCCTTCGGCCCTCGC"
b = "GCGAGGGCCGAAGGCCCGA"
## 
word = ["A","G","C","T"]
zlist = []
flist = []
for i in range(len(a)):   
    for j in word:
        t = list(a)
        t[i] = j
        tar = "".join(t)
        if tar ! =  a:
            zlist.append(tar)


for i in range(len(a)):
    for j in word:
        t = list(b)
        t[i] = j
        tar = "".join(t)
        if tar != b:
            flist.append(tar)
#rint(zlist)
#print(flist)

rightz = []
right = ["TCGGGCCTTCGGCCCTCGC"]
right = ["GCGAGGGCCGAAGGCCCGA"]


def find_motif(a):
    for i in open(a,"r"):
        if "seq" in i:
            name = i.split(">")[1].split("\n")[0]
            y = "y"
        elif y == "y":
            seq = i.split("\n")[0]
            for mismotif in zlist:
                a = seq.split(mismotif)
                s,e = 0,0
                if len(a) > 1:
                    for j in a:
                        s = len(j)+e
                        e = s+19
                        print(name+"\t"+str(s)+"\t"+str(e)+"\t"+"mismatch"+"\t+")
            for mismotif in flist:
                a = seq.split(mismotif)
                s,e = 0,0
                if len(a) > 1:
                    for j in a:
                        s = len(j)+e
                        e = s+19
                        print(name+"\t"+str(s)+"\t"+str(e)+"\t"+"mismatch"+"\t-")

            for motif in ["TCGGGCCTTCGGCCCTCGC"]:
                a = seq.split(motif)
                s,e=0,0
                if len(a) > 1:
                    for j in a:
                        s = len(j)+e
                        e = s+19
                        print(name+"\t"+str(s)+"\t"+str(e)+"\t"+"Complete"+"\t+")
            for motif in ["GCGAGGGCCGAAGGCCCGA"]:
                a = seq.split(motif)
                s,e = 0,0
                if len(a) > 1:
                    for j in a:
                        s = len(j)+e
                        e = s+19
                        print(name+"\t"+str(s)+"\t"+str(e)+"\t"+"Complete"+"\t-")
find_motif(sys.argv[1])

