from  collections  import Counter
mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,5,5,5]
print(Counter(mylist))
from collections import defaultdict
d={'a':10}
print(d)
print(d['a'])
from collections import namedtuple#use for name tuple  to find there values based on key
Dog=namedtuple('Dog',['age','name','bread'])
sam=Dog(age=5,bread="cake",name="sam")
print(sam)
print(sam[0])
