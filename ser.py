def search(list,n):
    i=0
    while i<=len(list):
        if list[i]==n:
          pos = i
          return True
        i=i+1
    return False
list=[1,2,4,5,7,9]
n=9
if search(list,n):
        print("search is found") 
        
else:
        print("not found")

#binary search in these all are must be sorted swaping the answer 
def sort(num):
     for i in range(len(num) -1,0,1):
          for j in range(i):
               if num[j] < num[j+1]:
                    temp=num[j]
                    num[j]=num[j+1]
                    num[j+1]=temp
num=[1,4,6,2,3]
sort(num)
print(num)
#another swaping method
def sort(num):
     for i in range(len(num)):
          minpos=i
          for j in range(i+1,len(num)):
               if num[j] < num[minpos]:
                minpose=j
     temp=num[i]
     num[i]=num[minpos]
     num[minpos]=temp
num=[4,1,9,5,3,6]
sort(num)
print(num)