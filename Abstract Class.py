#it is class with atleast one abstract method--method with no body
#+ we can't create object of abstract class
#python does'nt have inbuilt abstract class
#eg
class Com:
    def f(self):
        pass
c=Com()
c.f()# able to creat object
# To implement abstrac class
from abc import ABC,abstractmethod
class Com1(ABC):
    @abstractmethod
    def functioning(self):
        pass
    def g(self):
        print("helo")
#t=Com1() -- geting error
#what about child class?
class cpu(Com1):
    pass
#let see
#c1=cpu() --- geting error

# why abstract class?
#Let see
class cpu1(Com1):
    def functioning(self):
        print("yes cpu is functioning")
class Moniter(Com1):
    def display(self):
        print("displaying")
class check:
    def function(self,c):
        c.functioning()
c1=cpu1()
c1.functioning()
c2=Moniter()# i will not able to create this object if moniter is child of Com1 ,so it has to implement functioning method
ch1=check()
ch1.function(c2)   # it will not work if not make moniter chid of Com1 abdtract class
