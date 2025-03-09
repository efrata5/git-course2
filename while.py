#while loop
entry = 0 
sum = 0 
print("Enter numbers to sum, negative number ends list:") 
while entry >= 0: 
        entry = eval(input()) 
        if entry >= 0: 
           sum += entry 
print("Sum =", sum)
i=0
stop=int(input("enter a number :"))
while i<=stop:
      print(i)
      i+=1
#for loop

for n in range(10,1,-3):
   print(n)
#max *max multiplication table
max=5
#first print heading
print(end=" ")
#reverse of the words
for first in 'ABC':
     for second in 'ABC': 
      if second != first:
        for thrid in 'ABC':
            if thrid!=first and thrid !=second:
                print(first + second +thrid)
#break statement
i=1
while i<=4:
    if i%2==0:
        print(i)
        break
    i+=1
#infinite looping statement
max=3
n=1
while n>max:
    factor=1
    print(end=str(n) + ':')
    while factor <=n:
        if n % factor == 0:
            print(factor,end='')
            factor +=1
    print()
    n +=1

          
               