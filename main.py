
#exercies try and errors
try:
     for i in ['a','b','c']:
    
        print(i**2)
except TypeError as e:
    print("type error")

#queston 2
try:
    x=5
    y=0
    z=x/y

    print(x/y)
except ZeroDivisionError as e:
    print("undifiend")
finally:
    print('Alldone')
#problem 3
from math import*
def ask():
   
   while True:
       try:
            
        num=int(input("enter a integer number :"))#you have to write here in try unlse you cant print except value it show in compile error
         
       except ValueError as e:
           print("invalid input")
       else:
           break
   print(num*num)
       

ask()

