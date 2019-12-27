# 2019-11-27
# 学习python 第二天
# 浮点型尽量利用科学计数法，如：1.23乘以10的5次方=123000.0，可以写为1.23e5，10用e来表示0.0000123 可以用1.23e-5 表示
# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
# not True
# 输出 False
# Python的整数没有大小限制，Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
# python 中的列表list相当于java中的数组array，tuple元组相当于java中的list集合，list和元组都是有序的，list可变，tuple不可变
#
#
# 2019-11-28
# 学习python 第三天
# 函数的返回值类型不受限制，一个函数中多个return可以有多种类型
# 没有返回值的函数，调用时默认返回为None ，return None 简写为return:
# 返回多个参数的返回值是一个tuple
# 函数设置默认值power(x, n=2) 这样调用时n可以传也可以不传
# 函数的参数类型：必选参数、默认参数、可变参数、关键字参数和命名关键字参数 5种参数，顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#
# def person(*params) //可变参数
# def person(name, age, **kw) kw为命名关键字参数，
# 调动时可以省略：person('Michael', 30)，
# 也可以传入任意个参数：person('Bob', 35, city='Beijing')  、 person('Adam', 45, gender='M', job='Engineer')
# def person(name, age, *, city, job): * 号之后的city和job 为关键字参数的显示定义，说明调用时，必须传递这两个参数
# person('Jack', 24, city='Beijing', job='Engineer')  如果不这么写，会报错，如：person('Jack', 24, 'Beijing', 'Engineer') 会报错
# isinstance(x,A) 用来判断x是不是指定的 A 类型
# 利用生成器 打印 杨辉三角
#
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的
# Python的for循环本质上就是通过不断调用next()函数实现的
#
#
# 2019-11-29
# 学习python 第四天
# 函数式编程
# 难点 ： 闭包
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 闭包：函数内嵌套函数，通过return 返回内部函数（并且内部函数需要引用外部函数的变量，才是严格意义上的闭包，否则不算严格意义上的闭包）
# 调用闭包类型的函数时，需要变量接受，不然没有意义
# 闭包函数赋值给变量之后，变量多次调用，闭包函数内部信息是会保留累加的，可以实现类似“计数器”的功能
# 函数如果赋值给了变量，通过变量调用时，需要加() 括号 ： x() 表示调用函数
#
#
# 模块
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
#
# 2019-12-03
# 学习python 第六天
# 在非函数或类 声明的变量默认是glocal变量，在函数内部可以读取global变量，如果需要修改变量，则函数内部变量需要单独声明
# a = 100
# def fun01():
#     global a   #声明之后就可以修改全局变量a的值了
#     a=101  # 如果之前声明了global a 则会修改全局变量a的值，如果没有声明，则只是局部变量的赋值，并不会改变全局变量的值
#     print(a)
#     b = 103
#    def inner_fun():
#        nonlocal b # nonlocal 声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
#        b=104
#        print(b)
#    inner_fun()   # 内部函数之后调用之后才会生效
# fun01()
# print(a)  #这里的a是全局变量a
# 
#
# 2019-12-04
# 学习python 第七天
# 装饰器模式（对被装饰的对象（函数）进行功能的增强）
# 将被装饰的函数作为参数传入装饰函数，然后装饰函数return wrapper 赋值给被装饰的函数
#
# 2019-12-05
# 学习python 第八天
# 学习万能装饰器
# 装饰器可以多个
# 装饰器具有最近优先原则，哪个装饰的注解近先运行哪个
# 装饰器也可以传参数，传参时装饰器函数套3层
# def outer(a):
#     def decorate(func):
#         def wrapper(*args,**kwargs):
#             print("正在校验...")
#             time.sleep(2)
#             print("校验完毕")
#             func(*args,**kwargs)
#         return wrapper
#     print(a)
#     return decorate
#
# 默认赋值给a参数
# @outer(10)  
#
# 2019-12-06
# 学习python 第九天
# 匿名函数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数格式
# lambda 参数1,参数2..:运算
# s = lambda a,b:a+b
# 找出字典中a值最大的项
# list =[{'a':10,'b':30},{'a':30,'b':33},{'a':342,'b':20},{'a':23,'b':24}]
# print(max(list,key=lambda x:x['a']))
# reduce() 函数会对参数序列中元素进行累积。
# tuplel = (2,5,6,85,2)
# print(reduce(lambda x,y:x+y,tuplel))
#
# 2019-12-09
# 学习python 第十天
# 学习内置函数、匿名函数
# max
# min
# sorted
# map
# reduce
# filter
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#