# one function can return multiple value
# In python thier is no pass by value and reference
#if you pass a variable with immutable oject then by changing it id will change
def hey(x):
    print(id(x))
    x=8
    print(id(x))
a=10
print(id(a))
hey(a)
#type of actual parameters
def person(n,a):
    print(a-5)
    print(n)
#person(10,"har")  # it will give error
# type 1 --keyword parameters
person(a=10,n="har")
#what if not want to add age
def person1(n,a=18):
    print(a)
    print(n)
#type =DEFAULT
person1("har")
def sum(a,b):
    print(a+b)
# what if I wanyt to add more values
#type --3== variable lenth
def sum1(*a):
     c=0
     for i in a:
        c=c+i
     print(c)
sum1(1,2,3,45,6,5)
#function789+withlist
def count(l):
    c=0
    for i in l:
        if len(i)>5:
            c=c+1
    return c

l=["harind","aman","tshus","gdghhdj","deggduju"]
more5=count(l)
print("m5",more5)
