# def fed(x):
#     return x*x
#
# r = map(fed,[1,2,3,4])
# for i in r:
#     print(i)
#
# from functools import reduce
# def add(x, y):
#     return x + y
# print(reduce(add,[1, 3, 5, 7, 9]))
from day04.Student import Student

ddd = Student('Bart Simpson', 59)
ddd.print_score()