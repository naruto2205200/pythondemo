# def func(a):
#     s = a+a
#     def inner_func():
#         print(s)
#     return inner_func
#
# test01=func(1)
# test02=func(1)
# test01()
# test02()
# print(func(1))
# print(func(2))
# print(test01)
# print(test02)

def decorate(func):
    a =100
    print("wrapper 外层打印测试")
    def wrapper(*args, **kw):
        func()
        print("-----------")
    print("wrapper加载完成")
    return wrapper

@decorate
def house():
    print("============")

house()
# 添加注解之后就被装饰
print(house)