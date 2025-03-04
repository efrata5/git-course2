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