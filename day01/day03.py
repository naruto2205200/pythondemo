# def my_abs(x):
#     if(x>0):
#         return 32
#     else:
#         return "哈哈"
#
# print(my_abs(3))
#
# def my_none():
#     print("这是none")
#
# print(my_none())
#
# def my_abs2(x):
#     if not isinstance(x,(int)):
#         raise TypeError("bed operand type")
#
#
# 参数调用
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
# # num = ["sls","sfe"]
# person("zhangsan",10,*["sls","sfe"],city="beijing",job="IT")
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(10))
#利用 “切片” 实现字符串两端去空
# def trim(s):
#     if(len(s)==0):
#         return '空'
#     elif(s[:1]!=' ' and s[-1:]!=' '):
#         return s
#     elif(s[:1]==' '):
#         return trim(s[1:])
#     else:
#         return s
# s ='   rete   '
# print(trim(s))
#迭代
#Iterable 判断是否可以迭代
# from collections.abc import Iterable
# print(isinstance("abd",Iterable))
# # from collections import Iterable
# # isinstance("abd",Iterable)
#
# my_list = [(1,2,3),(4,5,8),(3,6,7)]
# for x,y,z in my_list:
#     print(x,y,z)
#
# for i,v in enumerate(my_list):
#     print(i,v)
#

# 列表生成式 高度灵活
# range(start,stop)可以生成 start 到stop 之间的所有整数，start不写的话默认为0
# for i in range(5):
#     print(i)
#
# my_list = list(range(4))
# print(my_list)
# 利用列表生成式 列出当前目录下的所有文件和文件夹
# import os
# print([d.u for d in os.listdir('.')])
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break