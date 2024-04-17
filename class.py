class computer:
       def __init__(self,b):
           self.b=b
           print("init")
       def add(self,a):
           print("hello",a+self.b)
       def j(self):
           print("hello",a+self.b)
a1 =computer(5)
a2=computer(10)
computer.add(a1,5)
a2.add(10)
a=5

'''class car:
    wheel=4
    def __init__(self):
        self.mdl=2401
        self.comp="hero"
    def  display(self):
        print(self.comp,self.mdl,self.wheel)
c1=car()
c2=car()
c1.display()
'''
