#operators
x=2
y=2
z=x+y
print(z)
z +=2
print(z)
c=x>y 
print(c)
c=x==y and x>y
print(c)
#converrting bonary to decimal
cb=bin(25)
print(cb)
cd=hex(24)
print(cd) 
cv=12&13
print(cv)
cg=12|13
print(cg)
cr=12^13
print(cr)
ch=25^30
print(ch)
import math
x=math.sqrt(25)
print(x)
y=math.floor(3.4)
print(y)
y=math.ceil(3.4)
print(y)
z=math.pow(2,3)
print(z)
import math as m
k=m.pow(2,4)
print(k)
#if statement and nested if
num=int(input("enter  a number : "))
print(num)

if num%2==0:
    print("number is even")
    if num>4:
        print("greater")
    else:
        print(" number is even but not greater")
else:
    print("odd") 
num=int("1")
while num<=5:
    print(num)
    num +=1

name=int("1")
while name<=5:
    print("hello")
    name +=1
#decremental
i=5
while i>=1:
    print(i)
    i -=1
#nested while loop
i=1
j=1
while i<=5:
    print("efrata",end=" ")
    while j <=3:
        print("enu",end=" ")
        j +=1
    i +=1
#for loop
x=["\n" "butu" "\n" "kiya"]
for i in x:
    print(i)
#pattern
for i in range (4) :
    for j in range(4) :
        print("#",end="")
    print()

for i in range(4):
    for j in range(i + 1):
        print("*",end="")

    print()
for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()
n=[10,25,68,90,46]
for b in n:
    if b%5 ==0:
        print(b)
        break
else:
    print("not found")
#array
import array as arr #you write these because python is not know array by default so you have to mention it
arr=("i",[1,2,3,4])
print(arr)
from array import* #now we can use any variable name here becuse astrick means you can use any vaariable name
arr=([])
n=int(input("enter the length of array :"))
for i in range(n):
    x=int(input("enter the value of x :"))
    arr.append(x)

print(arr)

n=int(input("enter the  value of search :"))
k=0
for k in arr:
    if k==n:
        print(k)
        break
k +=1
print(arr.index(n))

#summary for array
from array import *
num=([1,2,3])
print(num)
#by using for for array
from array import*
by=([1,2,3,7])
for b in range(2):
    print(b)
import numpy as np
array=np.array([[1,2,3],
      [4,5,6]])
print(array)
#copy arrays
from numpy import*
arr=[1,2,3]
arr2=arr
print(arr2)
print(arr)
print(log(arr))
print(max(arr))
arr3=sum(arr + arr2)
print(arr3)
#we are coping from the first array now we want different adress but they are the same number am gonna do now write view
print(id(arr))
print(id(arr2))

#working with matrix .ndim it gives dimmention and also .shape it gives the shape of rowa and columns and size it give the size of inside if you want to change 2 dimmentional in one dimentionale use dot flatted
from numpy import*
arr1=array([

        [1,2,3],
        [4,5,6]
           ])
print(arr1.ndim)
#shortcute you do not need separate array here is a shortcut to write a matric it give the size  of like the previous one
import numpy as np
m = np.matrix([[1,2,3,4],[7,8,9,10]])

print(m)
#function use always def to define function
def greating():
    print("good")
    print("morning")
greating()
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result=add_sub(5,4)
print(result)

def sent():
    print("what are you learnng about in this chapter")
sent()
def fav(c):
    
    print("one of my favourity thing in my life is raeding a " +c)
fav("bible")
def sar(a,*b):# astrick it  write  a lot of value n we can not tuple so we must use for
    c=a
    for d in b:
        c=c+d
        print(c)
sar(1,2,3,4)