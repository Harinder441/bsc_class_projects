class Student:
    def __init__(self,na,rn,lap):
        self.na=na
        self.rn=rn
        
    def show(self):
        print("name=",self.na)
        print("Roll no.=",self.rn)
        self.show()
    class Laptop:
        def __init__(self,comp,ram,hd):
            self.comp=comp
            self.ram=ram
            self.hd=hd
        def show(self):
            print(self.comp,self.hd,self.ram)

s1=Student("harinder",51,Laptop("dell",1000,4))
#s2=Student("Ravi",44)
s1.show()

