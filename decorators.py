#decorators
def hello(name):
        print("hellow function")
        def greet():
         print("i am yours friend")

        def welcome():
          print("never giveup just going")
        print(greet())
        print(welcome())
hello("efi")
#decorators
def div(a,b):
    print(a/b)
def smart_div(fun):
    def inner(a,b):
       if a<b:
         a,b=b,a
         return fun(a,b)
    
    return(inner)
div1=smart_div(div)
print(div1(2,4))
#decoratore it means we use indirect by typing inside
def hello():
      return "hello joea"

def other(some):
        print("amzing days")
        print(some())
other(hello)
