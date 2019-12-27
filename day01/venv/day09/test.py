from functools import reduce
a = lambda a,b:a*b
print(a)

list1 = [5,6,8,1,23,5]
print(max(list1))


# 匿名函数格式
# lambda 参数1,参数2..:运算
#
s = lambda a,b:a+b
print(s(1,2))
list =[{'a':10,'b':30},{'a':30,'b':33},{'a':342,'b':20},{'a':23,'b':24}]
print(max(list,key=lambda x:x['a']))

tuplel = (2,5,6,85,2,)
print(reduce(lambda x,y:x+y,tuplel))
