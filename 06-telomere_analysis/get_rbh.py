import sys

t1 = {}
for i in open(sys.argv[1]):
    a = i.strip().split("\t")
    if a[0] not in t1.keys():
        t1[a[0]] = a[1]

t2={}
for i in open(sys.argv[2]):
    a = i.strip().split("\t")
    if a[0] not in t2.keys():
        t2[a[0]] = a[1]

for i in t2.keys():
    if t2[i] in t1.keys():
        if t1[t2[i]] == i:
            print(i,t2[i])
