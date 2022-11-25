import sys
import numpy as np
from collections import Counter
def eucldist_vectorized(coords1, coords2):

    """ Calculates the euclidean distance between 2 lists of coordinates. """

    return np.sqrt(np.sum((coords1 - coords2)**2))

balance = [0.33,0.33,0.33]
A1sup = [0,0.5,0.5]
A2sup = [0.5,0,0.5]
Bsup = [0.5,0.5,0]
A1dom = [1,0,0]
A2dom = [0,1,0]
Bdom = [0,0,1]

balance_ = np.array(balance)
A1sup_ = np.array(A1sup)
A2sup_ = np.array(A2sup)
Bsup_ = np.array(Bsup)
A1dom_ = np.array(A1dom)
A2dom_ = np.array(A2dom)
Bdom_ = np.array(Bdom)




Category=["Balance","A1 suppressed","A2 suppressed","B1 suppressed","A1 dominant","A2 dominant","B1 dominant"]
def category(x):
    data = np.array(x)
    sample = []
    balance_dis = eucldist_vectorized(data, balance_)
    A1sup_dis = eucldist_vectorized(data, A1sup_)
    A2sup_dis = eucldist_vectorized(data, A2sup_)
    Bsup_dis = eucldist_vectorized(data, Bsup_)
    A1dom_dis = eucldist_vectorized(data, A1dom_)
    A2dom_dis = eucldist_vectorized(data, A2dom_)
    Bdom_dis = eucldist_vectorized(data, Bdom_)
    sample.append(balance_dis)
    sample.append(A1sup_dis)
    sample.append(A2sup_dis)
    sample.append(Bsup_dis)
    sample.append(A1dom_dis)
    sample.append(A2dom_dis)
    sample.append(Bdom_dis)
    index=(sample.index(min(sample)))
    return Category[index]

def Normal(data):
    normal = []
    for j in data:
        normal.append(j/sum(data))
    return normal

def run1(infile):
    out1=[]
    out2=[]
    for i in open(infile,"r"):
        a = i.strip().split("\t")
        mean = []
        name = a[0]
        genes = a[1:4]
        values = a[4:7]
        subs=[]
        for j in a[7:10]:
            subs.append(j[3:])   
        idxA1 = subs.index("A1")
        idxA2 = subs.index("A2")
        idxB1 = subs.index("B1")
        values = [values[idxA1],values[idxA2],values[idxB1]]
        values = list(map(float, values))
        normal=Normal(values)
        pattern = category(normal)
        out1.append(i.strip() + "\t" + pattern)
        out2.append(pattern)
    return out1, out2

out1,out2=run1(sys.argv[1])
#
if sys.argv[2] == "info":
    for i in out1:
        print(i)
if sys.argv[2] == "statis":
    c=Counter(out2)
    for i in c:
        print(i,c[i])
