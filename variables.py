#if the variables have same data then they have same address
a=23
b=a
print(id(a),id(b))
# id of data is same as variable
print(id(23))
#but
k=23
print(id(23))
#let see if we change  value
a=5
print(id(a))
# iF
k=a
b=7
# 23 is ready for garbage value
# we can't make variable const in python
#using type
print(type(k))
