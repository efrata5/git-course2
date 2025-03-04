#class
class computer:
    def config(self):
        print("i5,16gb,1TB")

com1=computer()
computer.config(com1)
com1.config()


#creating dog class will store the name and an age and we will give the dog ability to sit and roll when you given class you have to know that capitilaze the first letter
#initilizing name and age attributes

class Animal:
    def __init__(self,type):#intializing the attributes
        self.type=type
dog=Animal('Dog')
print(dog.type)
class Computer:
    def __init__(self,ram,cpu):
        self.cpu=cpu
        self.ram=ram
    def config(self): #these is a good way and simple way to call
        print("config is ",self.cpu,self.ram)
        
com=Computer("i5",16)
com2=Computer("ryne",8)
com.config() #these two are they used for calling
com2.config()

class Computer:
    def __init__(self):
        self.name="Efrata"
        self.age=22
        
    def update(self):
        self.age=30
    

    
c1=Computer()
print(c1.age)
c1.update()
print(c1.name)
print(c1.age)

#Types of variable
#1 instance it change when the value changes
class Car:
    wheels=4 #class variable and class instances
    def __init__(self):
        self.com="bmw"
        self.mile=10
c1=Car()
C2=Car()
c1.com="ethi"#here you can change it
Car.wheels=5 #you can change the class variable
print(c1.com,c1.mile,c1.wheels)
print(C2.com,C2.mile)
#types of method
#1 instance method
#2 class method
#3 static method
class Student:
    school="evan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1 + self.m2 +self.m3)/3
    @classmethod #it use for cls it means class it like decorators
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is a class of python")
s1= Student(32,45,67)
s2=Student(40,67,45)
print(s1.avg())
print(s2.avg())
print(Student.getSchool())#WE define in line 72 and it give the school name
Student.info()
#Iheritance of class
class Students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show() #we are define here the laptop

class Laptop: #Open another claa inside class
    def __init__(self):
        self.ram=8
        self.brand="hp"
        self.cpu="i5"
    def show(self):
        print(self.ram,self.brand,self.cpu)
        
s1=Students("Fetsa",2)
s2=Students("Ruth",3)
s1.show()
