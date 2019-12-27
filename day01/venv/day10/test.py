list1 = [1,5,8,6,7,5,8,2]
print(list(map(lambda item:item+1,list1)))

from functools import reduce
tuple1 = (2,5,8,6,4)
print(reduce(lambda x,y:x+y,tuple1))
result = filter(lambda x:x>5,list1)
print(list(result))