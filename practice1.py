from array import array
b=array("i",[])
print("enter=")
for i in range(5):
    b.append(int(input()))
print(b)
def dele(b,n):
    a=array(b.typecode,[])
    for i in b:
        if i!=b[n]:
            a.append(i)
    return a
b=dele(b,2)
print(b)
