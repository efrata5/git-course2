from main import*
def niu():
     print("keep going")
if __name__=="__main__":#the means not import for other only print here 
     niu()

#errors
def divi(x,y):
  try:#if these is not correct it jump on except and print
      print(x/y)
      k=int(input("enter a number K :"))
      print(k)
    


  except ZeroDivisionError as e:#when input zero it print these text there alot of value error text so you have to use for each different meaningfull valueerro types
           print("undefiend or zero is not divide by any number")
  except ValueError as e:#these one is for k when you enter a letter it print these text
       print("invalid input")
  print("bye")
x=int(input("enter  a number x :"))
y=int(input("enter a value y :"))
b=divi(x,y)
print(b)