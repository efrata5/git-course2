
# Use the generator

def square(n):
    for x in range(1,n+1):
        sqr=x*x
        yield sqr
for x in square(10):
    print(x)
import random
random.randint(1,10)
def rand_num()