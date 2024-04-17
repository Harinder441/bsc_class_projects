# how to iterate  over a dictionary
D={"punjab":"chd","HP":"Shimla","Haryana":"Chd"}
for k in D:
  print(k,"=",D[k])
  # Methods for dictionary
Dir={1:"North",2:"South",3:"East",4:"South"}
new=Dir.copy() # it returns a shallow copy of the original dict
print(new)
print(Dir.items())
print(new.keys())
print(new.values())
print(new.pop(3)) # pop() takes atleast one argument
print(new)
print(new.popitem()) # Popitem() takes no argument and bydefault it returns last pair
print(new)
# update method
d1={1:"A",2:"B"}
d={1,0}
d2={2:"C",3:"D",4:"E",5:"F"}
d1.update(d2)
print(d1)
x=all(d)
print(x)
# get()
Dir={1:"North",2:"South",3:"East",4:"South"}
print(Dir.get(5,"Not present"))
#Other built in fxns
Dir={1:"North",3:"South",2:"East",4:"South"}
Dir1={}
print(any(Dir1))
print(all(Dir1))
print(len(Dir))
print(sorted(Dir))
# Nested Dictinaries
StuDetails={20:{'name':'ram','class':'BCA','add':'xyz'},21:{'name':'sham','class':'MCA'}}
print(StuDetails[20])


