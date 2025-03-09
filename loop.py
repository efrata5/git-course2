#question 12 muliplicatin table
value=int(input("enter a value of table :"))
print(end='  ')
for column in range(1,value+1):
    print(end="%4d" % column)
print()
for column in range(1,value+1):
    print(end="----")
print('  +')
for row in range(1,value+1):
    print(end="%3d |" % row)
    for column in range(1,value+1):
        product=row*column
        print(end="%4d" % product)
    print()
#question 13 check palindorem
user=str(input("enter a word :"))
if user==user[:: -1]:
    print("it is palindrome")
else: 
    print("it is not palindrome")

#question 14 find factorial
n=int(input("enter a number :"))
factorial=1
for i in range(1,n+1):
    
        factorial*=i
print(factorial)
#question 15 find prime number
num=int(input("enter a number :"))
for i in range(2,num):
   if n%i==0:
       print("not prime")
       break
else:
       print("prime")
#question 16 find gcd
from math import*
num1=int(input("enter a number 1 :"))
num2=int(input("enter a number 2 :"))
print(gcd(num1,num2))
#question 17 revrese of a number 
from array import*
n=int(input("enter a number lengh of array :"))
arr=array('i',([]))
for i in range(n):
     x=int(input("enter a value of x :"))
     arr.append(x)
     print(arr)
for i in range(n-1,-1,-1):
        print(arr[i])