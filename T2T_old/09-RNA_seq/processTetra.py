import sys
import numpy as np
from collections import Counter


def eucldist_vectorized(coords1, coords2):

    """ Calculates the euclidean distance between 2 lists of coordinates. """

    return np.sqrt(np.sum((coords1 - coords2)**2))

balance = [0.25,0.25,0.25,0.25]
A1sup = [0,0.33,0.33,0.33]
A2sup = [0.33,0,0.33,0.33]
B1sup = [0.33,0.33,0,0.33]
B2sup = [0.33,0.33,0.33,0]
A1A2 = [0.5,0.5,0,0]
A1B1 = [0.5,0,0.5,0]
A1B2 = [0.5,0,0,0.5]
A2B1 = [0,0.5,0.5,0]
A2B2 = [0,0.5,0,0.5]
B1B2 = [0,0,0.5,0.5]
A1dom = [1,0,0,0]
A2dom = [0,1,0,0]
B1dom = [0,0,1,0]
B2dom = [0,0,0,1]

balance_ = np.array(balance)
A1sup_ = np.array(A1sup)
A2sup_ = np.array(A2sup)
B1sup_ = np.array(B1sup)
B2sup_ = np.array(B2sup)
A1A2_ = np.array(A1A2)
A1B1_ = np.array(A1B1)
A1B2_ = np.array(A1B2)
A2B1_ = np.array(A2B1)
A2B2_ = np.array(A2B2)
B1B2_ = np.array(B1B2)
A1dom_ = np.array(A1dom)
A2dom_ = np.array(A2dom)
B1dom_ = np.array(B1dom)
B2dom_ = np.array(B2dom)


Category=["Balance","A1 suppressed","A2 suppressed","B1 suppressed","B2 suppressed","A1A2 dominant","A1B1 dominant","A1B2 dominant","A2B1 dominant","A2B2 dominant","B1B2 dominant","A1 dominant","A2 dominant","B1 dominant","B2 dominant"]
def category(x):
    sample = []
    data = np.array(x)
    balance_dis = eucldist_vectorized(data, balance_)
    A1sup_dis = eucldist_vectorized(data, A1sup_)
    A2sup_dis = eucldist_vectorized(data, A2sup_)
    B1sup_dis = eucldist_vectorized(data, B1sup_)
    B2sup_dis = eucldist_vectorized(data, B2sup_)
    A1A2_dis = eucldist_vectorized(data, A1A2_)
    A1B1_dis = eucldist_vectorized(data, A1B1_)
    A1B2_dis = eucldist_vectorized(data, A1B2_)
    A2B1_dis = eucldist_vectorized(data, A2B1_)
    A2B2_dis = eucldist_vectorized(data, A2B2_)
    B1B2_dis = eucldist_vectorized(data, B1B2_)
    A1dom_dis = eucldist_vectorized(data, A1dom_)
    A2dom_dis = eucldist_vectorized(data, A2dom_)
    B1dom_dis = eucldist_vectorized(data, B1dom_)
    B2dom_dis = eucldist_vectorized(data, B2dom_)
    sample.append(balance_dis)
    sample.append(A1sup_dis)
    sample.append(A2sup_dis)
    sample.append(B1sup_dis)
    sample.append(B2sup_dis)
    sample.append(A1A2_dis)
    sample.append(A1B1_dis)
    sample.append(A1B2_dis)
    sample.append(A2B1_dis)
    sample.append(A2B2_dis)
    sample.append(B1B2_dis)
    sample.append(A1dom_dis)
    sample.append(A2dom_dis)
    sample.append(B1dom_dis)
    sample.append(B2dom_dis)
    index=(sample.index(min(sample)))
    return Category[index] 

def Normal(data):
    normal = []
    for j in data:
        normal.append(j/sum(data))
    return normal

#head=["Ortho_name","egg_A1","egg_A2","egg_B1","egg_B2","J2_A1","J2_A2","J2_B1","J2_B2","J3J4_A1","J3J4_A2","J3J4_B1","J3J4_B2","eFemale_A1","eFemale_A2","eFemale_B1","eFemale_B2","Female_A1","Female_A2","Female_B1","Female_B2","Cat_egg","Cat_J2","Cat_J3J4","Cat_eFemale","Cat_Female","Var"]

def run1(infile):
    out1=[]
    out2=[]
    for i in open(infile,"r"):
        a = i.strip().split("\t")
        mean = [] 
        name = a[0]
        genes = a[1:5]
        values = a[5:9]
        subs = []
        for j in a[9:13]:
            subs.append(j[3:])
        idxA1 = subs.index("A1")
        idxA2 = subs.index("A2")
        idxB1 = subs.index("B1") 
        idxB2 = subs.index("B2")
        values = [values[idxA1], values[idxA2], values[idxB1], values[idxB2]]
        values = list(map(float, values))
        normal=Normal(values)
        pattern = category(normal)
        out1.append(i.strip()+"\t"+pattern)
        out2.append(pattern)
    return out1,out2

out1,out2=run1(sys.argv[1])

if sys.argv[2] == "info":
    for i in out1:
        print(i)
if sys.argv[2] == "statis":
    c=Counter(out2)
    for i in c:
        print(i,c[i])




