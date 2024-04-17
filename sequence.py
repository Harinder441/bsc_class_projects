# 2+22+222+2222.......
'''n= int(input("enter value for n="))
a=0
i=0
sum=0
while (i<n):
    a=a*10+2
    sum =sum +a
    print(a,"+ ", end="")
    i=i+1
print("=")
print(sum)'''

'''
import numpy as np
A=np.random.randint(1,1000,100)

print(A)
A.sort()
print("After sorting",A)'''
#1 +(1+2)+(1+2+3)......

'''n= int(input("enter value for n="))
i=1
sum=0
elt=0
while (i<=n):

    elt =elt +i
    print(elt,"+ ", end="")
    sum=sum+elt
    i=i+1
print("=")
print(sum)'''
'''# random numbers
import numpy as np
A=np.random.randint(1,1000,100)
Le=[]
Lo=[]
print(A)
A.sort()
print("After sorting",A)
for i in range (100):
    if(A[i]%2==0):
        Le.append(A[i])
    else:
        Lo.append(A[i])
print("even=",Le)
print("odd=",Lo)'''
