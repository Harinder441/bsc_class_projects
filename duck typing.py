#eg
class A:
    def execute(self):
        print("hey I am A")
class B:
    def execute(self):
        print("hey I am B")
class C:
    def __init__(self,alpha):
        alpha.execute()
a=A()
b=B()
c=C(a)
d=C(b)
