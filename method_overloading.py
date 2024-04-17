# as in python variable type is not spcified
#+ func with same name decalared after existing  func with that name overide the existing func
#so method overloading is not possible in python
#alternatives
#1
def sum(a=0,b=0,c=0,d=0):
    sum=a+b+c+d
    print(sum)
sum(1,2,4,5)
