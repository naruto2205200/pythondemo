lsit1 = [1,5,8,6,7,5,8,2]
print(list(map(lambda item:item+1,lsit1)))

from functools import reduce
tuple1 = (2,5,8,6,4)
print(reduce(lambda x,y:x+y,tuple1))