# data type in python we can not use rhe comma to separte nubers instead we use underscore
a=20
print(type(a))
b=5.6
print(type(b))
from math import*
a=216
print(bin(a))
print(oct(a))
print(hex(a))
x=123_35678_7890
print(x)
y=('100',2)
print(y)
z=5+2j
print(type(z))
v=str(8)
print(v)
#look the diffrence and the impact of single and double qoutation marks
a=892+800
print(a)
b='892'+'800'
print(b)
c='efi'+'efi'
print(c)
x=12
print("x =",x)
x,y,z=90,60,70
print("x = ",x ,"y = ",y ,"z = ",z)
ava=6.022e23
print(ava)
num=eval(input("enter a number :"))
print(type(num))
n1=eval(input("enter a number 1 :"))
n2=eval(input("enter a number 2 :"))
print("the sum of two number is =",n1+n2)
n=int(input("enter a number :"))
b=float(input("enter a number"))
print(n+b)
a,b,c,d=10,20,30,40
print(a,b,c,d,sep=',')
print(a,b,c,d, sep=':')
print(a,b,c,d, sep='')
print(a,b,c,d,sep='---')
a=10
b=3
print(a%b)
print(a//b)
x=5
b=4
z=a<b
print(z)
a=0
b-1
z=a!=0 and (b/a)>0
print(z)
c=5
d=3
e=c^d
print(e)
#if statement
divided=eval(input("enter a first number : "))
divisour=eval(input("enter a divisour number : "))
if divisour !=0:
    d=divided/divisour
    print(d)
else:  
     print("not divide")
a,b,c,d=20,20,30,30
if a==b:
    
      if c==d:
           
         print("same")
      else:
               print("they are not the same")
#by using if and else write a good  dialog
j="hi there may i ask you a quistion?"
print(j)
niya=str(input("hi there "))
yes="giving permition"
if niya==yes:
     print("yes you can")

else:
     print("no you can  not")
#months
month=int(input("enter a numbers of months(1/2/3/)"))
if  month==1:
     print("feburary")
elif month==2:
     print("march")
elif month==3:
     print("june")


#while loop
i=0
while i<5:
     print(i)
     i+=1
    