S={n for n in range(10)}
print(S)
S1=set([1,2,2,3,2,1])
print(S1)
S.update(['a','b'])
print(S)
S.remove(2)
print(S)
S.discard(2)
print(S)
if (2 not in S):
  print("yes")
else:
  print("no")
