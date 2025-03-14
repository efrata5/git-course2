#question 30 creat a list
user=[]
number=int(input("enter a  length number :"))
for b in range(number):
    x=int(input("enter a list of numbers :"))
    user.append(x)
    print(user)
#question 32 access elemnt of the list the first and the last
user1=[]
number=int(input("enter a length of the list :"))
for c in range(number):
    y=int(input("enter a number of a list :"))
    user1.append(y)
    print(user1)
first=user1[0]
last=user1[-1]
print(first,last)
# question 33 append element in the list
country=["ethiopa","kenya","sudan"]
country.append("usa")
country.append("italy")
country.append("uganda")
print(country)
# question 34 insert element
numbers=[1,5,9,11]


numbers.insert(1,3)
numbers.insert(3,7)
print(numbers)
# 35 question 