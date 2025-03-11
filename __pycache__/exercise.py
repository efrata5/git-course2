list=[1,2,3,4]
list3=list*3
print(list3)
list=3 in list
print(list)
quote="what"
string_to_list=str(quote)
print(string_to_list)
vegetable=["caraote","potato","carbage","tommato"]
print( vegetable[::2])
river=["awash","abaya","tan"]
print(len(river))
number=[1,2,3,4]
print(sum(number))
print(max(number))
print(min(number))
print(any([0,0,0,0]))
print(all([0,0,0]))
sorted=sorted(river)
print(sorted)
#continued
country=["addis","jimma","usa","newyork"]
print(country.count("addis"))
print(country.index("addis"))

country.append("poland")
print(country)
country.sort()
print(country)
counrt1=["gambela","jinka"]
country.extend(counrt1)
print(country)
#pupulating items
fruits=["mango","appel","orange"]
for i in fruits:
    print("i like to eat",i)
#nested list [[]] by these symbol
counting=[[1,2,3],
          [4,5,6],
          [7,8,9]

]
print(counting[0][1])
#deleting from the list
n=[1,2,3,4,5]
del n[2]
print(n)
del n[3:4]
print(n)
#sorting
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[65,56,1,90,4,7]
sort(list)
print(list)
#selection sort
def sort(num):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if num[j]<num[minpos]:
                 minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
num=[9,6,10,1,3,0]
sort(num)
print(num)