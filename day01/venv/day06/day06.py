# a = 100
# def fun01():
#     global a # 这里默认的是local变量，并没有改变函数外部的a的值
#     a = 101
#     b = 103
#     def inner_fun():
#         global a
#         nonlocal b
#         b=104
#         a=102
#         print(a)
#     inner_fun()
#     print(a)
# fun01()
# print(a) #这里的a是全局变量a，a的值并没有改变
def func():
    a = 10
    def inner_func():
        print(a)
    return inner_func
x = func()
x()