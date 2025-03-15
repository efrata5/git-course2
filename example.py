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
class Dog(Animal):
    def __init__(self):
        super().__init__()#here it prinit animal created
        print("dog created")
    def who_am_i(self):
        print("i am a dog")
        
d=Animal()
e=Dog()
e.who_am_i()
d.who_am()
d.i_eat()
class Pycharm:
    def execute(self):
        print("running")
        print("coding")
class Mystudy:
    def execute(self):
        print("walkiing it like a duck")
        print("running")
        print("coding")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Pycharm()
ide=Mystudy()
lap1=Laptop()
lap1.code(ide)
lap1.code(ide)

class Book:
    def __init__(self,title,author,page):
        self.author=author
        self.page=page
        self.title=title
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.page
b=Book('neverstop','joel',200)
print(b)
print(len(b))
#homework
class Mathe:
    def __init__(self,cor1,cor2):
        self.cor2=cor2
        self.cor1=cor1
    
    def distance(self):
        return self.cor1 +self.cor2
    def slope(self):
        return (self.cor2[1]-self.cor1[1])/(self.cor2[0]-self.cor1[0])


d=Mathe((3,2),(4,5))
print(d.distance())
print(d.slope())
#account

class Account:
     bank="awash"
     def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner
        
     def deposit(self, dep_amt):

      self.balance += dep_amt
      print(f"Deposited: {dep_amt}. New balance: {self.balance}")

     def withdraw(self, withdraw_amt):

        if self.balance >= withdraw_amt:
           self.balance -= withdraw_amt
        print(f"Withdrew: {withdraw_amt}. New balance: {self.balance}")
     @classmethod  
     def info(cls):
         return cls.bank


d = Account("Habti", 400,)



d.deposit(200)
d.withdraw(50)
print(Account.info())
from colorama import init,Fore
init()
print(Fore.RED + "efi")
