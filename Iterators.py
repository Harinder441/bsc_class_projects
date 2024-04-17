class abc:
    def __init__(self):
        self.alpha=97
    def __iter__(self):
        print("hello")  #doubt about iter method
        return self
    def __next__(self):
        if self.alpha<=122:
            v=self.alpha
            self.alpha=self.alpha+1
            return chr(v)
        else:
            raise StopIteration
a1=abc()
print(a1.__next__())
print(a1.__next__())
for i in a1: # in behind iter and next are working
    print(i)

