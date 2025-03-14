class Computer:
    def __init__(self,ram,cpu):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        
        print(self.ram,self.cpu)
c1=Computer(5,"i5")
c1.config()
class Dog:
    def __init__(self,name,spots,bread):
        self.name=name
        self.spots=spots
        self.bread=bread
    def config(self):
        print(self.name,self.bread,self.spots)

c2=Dog("buchi","cake",5)
c2.config()
from math import*
class Cricle:

    def __init__(self,radius):
        self.radius=radius
    def circumstances(self):
        
        return self.radius*pi*2
        
c4=Cricle(2)

print(c4.circumstances())
class A :#it is called super
    def __init__(self):
        print("git ini A")
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B(A):#inheritance  of A it include all in A
    def __init__(self):
        super().__init__()#HERE IT PRINT ALSO IN A 

        print(" git init B")#at these time it print only b not a if you want to print also in a
        
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")

c=A()
c.feature1()
c.feature2()
d=B()
d.feature3()
d.feature4()
d.feature1()
d.feature2()
class Animal:
    def __init__(self):
        print("Animal created")
    def who_am(self):
        print("i am an animal")
    def i_eat(self):
        print("i eat food")
d=Animal()
d.who_am()
d.i_eat()