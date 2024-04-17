from numpy import round
#calculating difference
def difference(Y):
    L=[]
    for i in range(len(Y)-1):
        L.append(round(Y[i+1]-Y[i],4))
    return L
def diffD0(Y):
    # making difference table and storing 1St value of every colon  in D0
    D0=[Y[0]]
    K=Y
    while len(K)!=1:
        K=difference(K)
        D0.append(K[0])
    return D0

#to construct u(u-1)...(u-(n-1))(u-n)
def ufunc(n,x,X):
    # calculating value of h and u
    h=X[1]-X[0]
    u=(x-X[0])/h
    if n==0:
        return u
    else:
        return (u-n)*ufunc((n-1),x,X)
# to construct n!
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
#To construct D0[0]+uD0[1]/1! +.....+u(u-1)...(u-(n-1))D0[n]/n!
def f2(n,x,X,Y):
    D0=diffD0(Y)
    if (n==0):
        return D0[0]
    else:
        return (ufunc(n-1,x,X)*D0[n])/fact(n) + f2(n-1,x,X,Y)
