class langrange:

    def __init__(self,X,Y,x):
        self.X=X
        self.Y=Y
        self.x=x
    #to construct  n!=n1multi(x-xn)
    def nfunc(self,n,n1):
        if(n==-1):
            return 1
        elif(n==n1):
            return self.nfunc(n-1,n1)
        else:
            return (self.x-self.X[n])*self.nfunc(n-1,n1)

    #to construct n1!=n multi(xn1-xn)
    def dfunc(self,n,n1):
        if(n==-1):
            return 1
        elif(n==n1):
            return self.dfunc(n-1,n1)
        else:
            return (self.X[n1]-self.X[n])*self.dfunc(n-1,n1)
    #to construct (nfunc(n,0)/dfunc(n,0))*y[0]+(nfunc(n,1)/dfunc(n,1))*y[1]#
    #--------(nfunc(n,n1)/dfunc(n,n1))*y[n1]

    def func(self,n,n1):
        if(n1==-1):
            return 0
        else:
            return ((self.nfunc(n,n1)/self.dfunc(n,n1))*self.Y[n1])+self.func(n,n1-1)
    def display(self):
        n=len(self.X)-1
        n1=len(self.Y)-1
        y=self.func(n,n1)
        print("y=",y)
X=[1985,1987,1989,1991,1993]
Y=[40,43,48,52,57]
x=1992
c1=langrange(X,Y,x)
c1.display()
