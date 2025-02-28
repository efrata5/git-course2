print("hello world")
# basic python and variable

message="hi there"
print(message)
name="Efrata"
print("my name is " +name)


character="you"
print(character.title())
print(character.lower())
print(character.upper())



#working string with python
phrase="giraffe acadamy"
print(phrase)

phrase="giraffe acadamy"
print(phrase + " is cool")
print(phrase.index("a"))
print(phrase.replace("giraffe","elephant"))

#working with number
print(3+4+5)
my_num=-5
print(abs(my_num))

#user input
message=input("write something I will reapeat back to you ")
print(message)
name=input("enter your name")
print("hello " + name)

age=input("enter your age")
age=int(age)
print(age)

if age>=18:
    print("you can vote")
else:
    print("you can not vote")
num1=int(input("enter a number one :"))
print(num1)
num2=int(input("enter number two :"))
print(num2)
operators=input("choose maths operators (sub, mult,add): ")
print(operators)
if operators == "sub":
    result = num1-num2
    print(result)
elif operators == "mult":
    result = num1*num2
    print(result)
elif operators == "add" :
    result = num1 + num2
    print(result)
else:
    print("invalid ")  




shopping=("welcom to our shopping center ! \n what would you like to buy")
print(shopping)
item="1.add an item"
print(item)
shopp=("what you like to buy")
print(shopp)
shopping_list=input("enter your choice (1/2/3)")
print(shopping_list)

if shopping_list == "1":
    
    print("apple")
elif shopping_list == "2":
    print("banna" "\n" "apple")
    
elif shopping_list == "3":
    print("apple" "\n" "banna" "\n" "orange")
    