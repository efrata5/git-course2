#if statement if is in python  suit
#accepting students grade based on the mark out the grade

mark=int(input("enter your mark out of hundered : "))


if( mark>=85):
    print("A")
elif(mark>=75 ):
    print("B")
elif(mark>=65 ):
    print("C")
elif(mark>=40):
    print("D")

else:
    print("you are not passed")
#while loop
i=0 #initializing
while i<=2:#condition
    print("hello")
    j=1
    while j<=3:
        print("hi")
        j +=1
    i +=1 #increment or decrement
 #forloops it use for sequences the output it gives line by line range(10) means start for zero and end in nine they are 10 ranges
for  i in range(12,20,1):#these means starting from 12 and it increase by 1 the end is 20
    print(i)
for i in range(5,7,1):
    print(i)
for i in range(1,21):
        if i%5!=0 :
            print(i)
        
#exercise 
x =int(input("How many candidated"))
i=1
while i<x:
    print("candidates",i)
    i +=1
ave=6
num=int(input("how many candidates :"))
i=0
while i<=num:
    if i>ave:
      print("out of stock")
    break
    
    print("canday")
    i +=1
  
print("bye")