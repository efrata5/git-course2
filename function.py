#function
#21 area of circle
from math import*
def circle(r):
 
    return area

r=float(input("enter radius :"))
area=r*r*pi
area=circle(r)
print(area)
# question 22 even or odd
def even_odd(num):
    if num%2==0:
        return "even"
        
    else:
        return "odd"
num=int(input("enter a number :"))
evod=even_odd(num)
print(evod)
#question 23 celius to farantite
def celi(c):
    fahrenheit=(c*9/5)+32
    return fahrenheit

c=int(input("enter a celius degree :"))
degree=celi(c)
print(degree)
#question 24 check palindrome
def pali(word):
    if word==word[::-1]:
        return "palidrom"
        
    else:
        return "not palidrome"
        

word=str(input("enter a word :"))
sent=pali(word)
print(sent)
#question 25 factorial
def fac(n):
    
        return fact
n=int(input("enter a number :"))
fact=1
for i in range(1,n+1):
     fact*=i
facts=fac(n)
print(facts)
# question 26 GCD
from math import*
def common(n1,n2):
     return gcd(n1,n2)
n1=int(input("enter a number 1 :"))
n2=int(input("enter a number 2 :"))
commons=common(n1,n2)
print(commons)
# question 27 revrese of a string
def rev(word):
     return word[:: -1]
word=str(input("enter a word :"))
reverse=rev(word)
print(reverse)
#question 28  print pattern
def patr(n):
    
  for i in range(n):
     
     for j in range(n-i):
          print("*",end=" ")
     print()
n=int(input("enter a number :"))          
patr(n)
