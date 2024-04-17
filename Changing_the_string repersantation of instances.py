class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x}, {0.y})'.format(self)
    def __str__(self):
        return '({0.x}, {0.y})'.format(self)
p=Pair(1,2)
q=int(23.78)
print(str(p))
print(str(q))

i=54556.00
print(str(i)+"hello")
s='helo'
print(repr(s))
