# 通过装饰器完成登录校验
import time
# 万能装饰器，被装饰函数可以传参也可以不传参
def outer(a):
    def decorate(func):
        def wrapper(*args,**kwargs):
            print("正在校验...")
            time.sleep(2)
            print("校验完毕")
            func(*args,**kwargs)
        return wrapper
    print(a)
    return decorate

@outer(10)
def login1():
    print("login1...")

def login2():
    print("login2...")
login2()
login1()
