def sum(*b): #variable length argument
    s=0
    for i in b:
        s=s+i
    print(s)
sum(1,2,4,56,4)
