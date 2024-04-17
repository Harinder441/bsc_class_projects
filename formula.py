
def ufunc(u,n):
    if n==0:
        return u
    else:
        return (u-n)*ufunc(u,(n-1))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=len(D0)
def f2(n):
    if (n==0):
        return D0[0]
    else:
        return (ufunc(u,n-1)*D0[n])/fact(n) + f2(n-1)
