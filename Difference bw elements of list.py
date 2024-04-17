import numpy as np
l1=[1,2,3]
l2=[1,3,5]
d=[]

for i in range (0,3):
    for j in range (0,3):
        diff = np.abs(l1[i]-l2[j])
        d.append(diff)
print(d)
print(min(d))
for k in range (0,3*3):
    if d[k]== min(d) :
        print("pair is",l1[k-2],l2[k])
