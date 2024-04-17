class A :
    def __init__(self):
        print("u r in A")
    def F1(self):
        print("Feature 1 working")
    def F2(self):
        print("Feature 2 working")
class B :

    def F3(self):
        print("Feature 3 working")
    def F4(self):
        print("Feature 4 working")
class C(A):
    def __init__(self):
        self.b=5
        print("u r in C")
        super().__init__()
        super().F1()
    pass
a=C()
print(a.b)
