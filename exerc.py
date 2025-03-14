name="hello"
print(name)
print(name[0])
#we can not change index by there indexing number we change the by concatination
name="abel"
print("p" + name)
x='hello world'

print(x + " it is a beutifull outside")
#format method
y="data structure"
print(y+ format(" alogorithm"))
print( "The {}{}{}" .format("fox ","brown "," color") )
#format method by floating
result=3/12
print("the is {r:1.3f}".format(r=result))
#if statement
loc='bank'
if loc=='bus':
    print("it is true")
elif loc== 'bank':
      print("balk")
else:
    print("it is false")
#for loop

list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
     if i%2==0:
          print(i,end=",")
list_sum=0
for i in list1:
    list_sum=list_sum +i
print()
print(list_sum )
#string
string="my"
for _ in string:
     print("cool")
#dictionary
d={"k":1,"b":2,"c":3}
for key,value in d.items():
     print(key)
#tuple
number=[(1,2,3),(4,5,6,)]   
for a,b,c in number:
     print(b)
#pass
numbers=[1,2,3,4,5]
for i in numbers:
     
          pass
print("good job")

#shuffle
import random
number=[1,2,3,4,5,6]
random.shuffle(number)
print(number)
#exercise
name="samson"
for i in  name:
     if i == "s":
       print(name.split("s"),end="")
#question 2
for i in range(0,10):
     if i%2==0:
          print(i)
#question3  string
name="efrat"
if len(name)%2==0:
     print("even",len(name))
else:
     print("odd",len(name))
#question 4
for i in range(1,100):
     if i%3==0:
          print("buss")
     elif i%5==0:
               print("fizz")
     elif i%3==0 and i%5==0:
                  print("fizzbuss")
               
    