# 2. String case changing methods
#a) capitalize()
S="hello everyone"
print(S.capitalize()) # return string with first letter capitalized
#b) lower()
S1="HELLO"
print(S1.lower())
#c) upper()
# d) title()
S="hello everyone"
print(S.title())
# e) swapcase() LC <-> UC
S="Hello"
print(S.swapcase())
# type 3: String Stripping methods
# a) strip() (bothside)
S="    Python**is**fun  "
print(S.strip())
# b) lstrip()
S="********Python**is**fun****"
print(S.lstrip('*'))
# c) rstrip()
# type 4: String searching methods
# a) endswith(string,start,end) # from where to start and stop searching
S1="welcome to the world of python to akal uni"
print(S1.endswith('python'))
print(S1.endswith('world',2,20))

# b)startswith()
# c) find() "returns -1 if not found else returns the index value"
print(S1.find('for'))
# d) rfind()
print(S1.rfind('to'))
# e) index()
print(S1.index('to')) #"give value error if not found else returns the index value"
# f) rindex()
print(S1.rindex('to'))
# String splitting methods
# a) split(sep,maxsplits(-1)) # if sep is not defined then whitespace character is used as default delimeter
S="welcome to python"
print(S.split(' ',1))
S1="www.google.com"
print(S1.split('.'))

#b) rsplit(sep,maxsplit)
S="welcome to python"
print(S.rsplit(' ',1))

# c) partition(sep)
S="working with python is fun"
print(S.partition(' '))
print(S.partition('$'))
# d) rpartition

print(S.rpartition(' '))
print(S.rpartition('$'))

# e) splitlines([keepends]) \n

S3="working\nwith\npython\nis\nfun"
print(S3.splitlines())
print(S3.splitlines(True))
# string replacing methods
# a) replace(old,new)
S="welcome to python"
print(S.replace("python","c++"))

# b) expandtabs(tabsize)# bydefault tabsize=8
S1="welcome\tto\tpython"
print(S1.expandtabs(12))
# string formating methods
#a) center(width,[ch])
S="hello"
print(S.center(20,'*'))
# b)ljust(width,[ch])
print(S.ljust(20,'$'))
# c) rjust()
print(S.rjust(20,'$'))

# d) format() - used for variable substitution using placeholder {}
S="He wants {} icecream {}"
print(S.format(2,'vanilla'))
S1="He wants {1} icecream of {0} flavour for {2} rupees" # indexing
print(S1.format('choclate',1,10))

marks=[50,55,60]
S2="marks of 3 studends {},{} and {}"
print(S2.format(*marks))
# 1. join(seq)  # where seq is List of string
s="working with python is fun"
L=s.split()
print(L)
L1=" " #creates an empty string
print(L1.join(L))

# 2. zfill(width) #returns a copy of string that is left padded with 0 digit.
s="+working with python is fun"
print(s.zfill(40))
