class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def config(self):
        print("my name is " + self.name ,self.age)
c1=Student("efrata",22)
c1.config()
class Computer:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
    def config(self):
        print( self.ram,self.cpu )
c2=Computer(8,"i5")
c2.config()
class Student1:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
d2=Student1(2,3,4)
print(d2.avg())
class Teachers:
    def __init__(self,postion,age,gender):
        self.gender=gender
        self.postion=postion
        self.age=age
        self.office=Office()
        
    def show(self):
        print("the information of applyers and age and gender"+self.gender,self.postion,self.age)
        self.office.show()

class Office:
    def __init__(self):
        self.office="rama"
        
    def show(self):
        print(self.office)

jim=Teachers(34,"direcor","f")
jim.show()
#polymorphis it means one thing with  multiple form  types duck typing,operator overloading,method overloading,method overridding
#duck typing is one thing but a lot of forms to describe
class Pycharm:
    def execute(self):
        print("complinig")
        print("running")
class Myeditor:
    def executes(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")
class Laptop:
    def code(self,ide):
        
        ide.executes()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)
#maths operators
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):#for all maths operator we do the same like only change the add for greater than use gt
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=Student(m1,m2)
        return s3
s1=Student(2,3)
s2=Student(4,5)
s3=s1 +s2

print(s3.m2)
#methods of overloading
class Student1:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:

           s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=c
        return s
s1=Student1(5,6) 
print(s1.sum(9,8,7))
#method overridding
class A:
    def show(self):
        print("in A show")  
class B(A):
    def show(self):
        print("in B show")
a1=B()
a1.show()
#iterators
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        val=self.num
        if self.num<=10:
            self.num +=1
            return val
        else:
          raise StopIteration
values=TopTen()
for i in values:
    print(i) 

#yield
def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n +=1
values=topten()
for i in values:
    print(i)
