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

#user if statement by usr input
message=input("write something I will reapeat back to you ")
print(message)
name=input("enter your name :")
print("hello " + name)

age=input("enter your age :")
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
shopping_list=input("enter your choice (1/2/3) :")
print(shopping_list)

if shopping_list == "1":
    
    print("apple")
elif shopping_list == "2":
    print("banna" "\n" "apple")
    
elif shopping_list == "3":
    print("apple" "\n" "banna" "\n" "orange")
else:
    print("invalid")
    #variables simple examples
print("navini's ")
name=("my name is EFrata ")
print(name)
message=("what are you doing now")
print(message)
good=("keep going you are good now")
print(good)
good=("youtube")
print(good[0:2])
print(good[0 :])
print(good[ :6])
first_name="Efrata"
second_name="gebrameskel"
print(first_name + " "  + second_name.lstrip())
text='hello efi "would you like to learn python today"'
print(text)
message="efi"
print(message.lower())
print(message.upper())
print(message.title())
person_name='Alberte said, "a person who never made a mistake never tried annything again" '
print(person_name)
print(5+3)
print(12-4)
print(2*4)
print(16/2)
num="2"
print(num +" is my favourite number")

#list 
name=["Alazare","Baroc","Yordi"]
print("hello " + name[0] )
print("hello " + name[1])
print("hello " + name[2])
num=["2","3","4"]
print(num)
print(num[0])
number=[2.3,"efrata",5]
print(number)
car=["toyota","vitize","suzuki"]
print(car)
car[0]="taxi"
print(car)
car.append("bajaja")
print(car)
car.append("hiluk")
print(car)
motorcycle=[]
motorcycle.append('honda')
motorcycle.append("ducati")
motorcycle.append("yamaha")
print(motorcycle)
motorcycle.insert(0,"suzuki")
print(motorcycle)
del motorcycle[0]
print(motorcycle)
del motorcycle[1]
print(motorcycle)