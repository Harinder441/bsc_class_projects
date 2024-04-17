class mod7:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        b=self.a+other.a
        c=b%7

        return c
a=mod7(3)
b=mod7(8)
print(a+b)

