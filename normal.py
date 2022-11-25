## calculate noramlized depth for each windows

import sys
import numpy as np

dic = {}
tmp = []
dp_list=[]
#change index in dp 
for i in open(sys.argv[1]):
    a = i.strip().split("\t")
    dp = int(a[4])/int(a[6]) ## depth for windows
    dp_list.append(dp) 
    tmp.append(a)

dp_wg = np.median(dp_list) ## dp for whole genome
x = 0
for j in tmp:
    x = x +1 
    name = "Windows_" + str(x) # window name 
    normaldp=int(j[4])/int(j[6])/dp_wg
    print(name + "\t" + j[3] + "\t" + str(normaldp))
    
