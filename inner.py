class Student:
    class Laptop:
        def __init__(self,brand,ram):
            self.ram=ram
            self.brand=brand
        def show(self):
            print(self.ram,self.brand)
    def __init__(self,name,age):
            self.name=name
            self.age=age
            self.lap=self.Laptop(8,"hp")
    def show(self):
            print(self.name,self.age)
            self.lap.show()
s1=Student("Efrata",22)
s1.show()
#exercise doctore and client
class Doctore:
     class Patient:
          def __init__(self,name,age,adress,phone):
               self.name=name
               self.age=age
               self.adress=adress
               self.phone=phone
          def show(self):
               print("patient",self.name,self.age,self.adress,self.phone)
     def __init__(self,name,position,adress):
          self.name=name
          self.position=position
          self.adress=adress
          self.pat=self.Patient("Hayilu",30,"jimma",'09678956')
     def show(self):
          print("lung doctor",self.name,self.position,self.adress)
          self.pat.show()
d1=Doctore("Tedy","doctore","jimma")  
d1.show()  
#global and local variable
a=10
def some():
     global a
     a=15
     print("is fun :",a) 
    
some()  
print("outside :",a)       
#milistone game
import random
suits=('spade','hearts','diamond','club')
ranks=('two','three','four','five','six','seven','eight','nine')
values={"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"king":22,"j":12}#we ddefine here integres when we write a value it shows integer value
class Card:
     def __init__(self,suit,rank):
          self.suit=suit
          self.rank=rank
          self.value=values[rank]
     def __str__(self):
          return self.rank + " of " + self.suit
class Deck :
     def __init__(self):
         self.all_cards=[]

         for suit in suits:
          for rank in ranks:
                    #create the card object
               created_card=Card(suit,rank)
          self.all_cards.append(created_card)#there is a mistake here it not changeinge the rank number
     def shuffle(self):
          random.shuffle(self.all_cards)
     
     def deal_one(self):
          return self.all_cards.pop()
class Player:
     def __init__(self,name):
          self.name=name
          self.all_cards=[]
     def remove_one(self) :
        return self.all_cards.pop()
     def add_card(self,new_cards) :
          if type(new_cards)== type([]) :
              #list multiple  object
              self.all_cards.extend(new_cards)
           #for a single card object
          else:
               self.all_cards.append(new_cards)  
     def __str__(self) :
         return f"player {self.name}  has {len(self.all_cards)}" 
player_one=Player("one")
player_two=Player("two")
new_deck=Deck()
new_deck.shuffle()
#while game_on
for x in range(26):#half of 52
     player_one.add_cards(new_deck)

print(len(new_deck.all_cards))

mycard=new_deck.deal_one()

print(mycard)
print(len(new_deck.all_cards))
new_player=Player("jose")
print(new_player)
new_player.add_card(mycard)#here we are connceting from the first one 
print(new_player)
print(new_player.all_cards[0])
new_player.add_card([mycard,mycard,mycard])# here we add for joes  noe he has 4  we add in 97 line 
print(new_player)
#game setup

