#lists
greating=["good morning","good afternoon","hello "]
greating[0]="hi there"
print(greating)
fas_food=["doro","kitfo","tibise"]
for i in fas_food:
    print("i like ",i)
#search in the list the first 1 is leaner search
def search(list,n):
     i=0
     while i<len(list):
          if list==n:
               return True
          i+=1

          return False
list=[1,2,3,4,5,7]
n=9
if search(list,n):
     print("found")
else:
     print("not found")
#do by using for loop
def search(list,n):
     list=[1,2,3,4,5]
     n=2
     for i in len(list):
          if list ==n:
               return True
          return False


if search(list,n):
     print("found")
else:
     print("not found")
