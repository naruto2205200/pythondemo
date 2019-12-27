# person="孙悟空"
# phone="15888888888"
# age = 20
# print("姓名：%s，年龄：%s，联系电话：%s" %(person,age,phone))
# print("年龄："+str(age))
# year=2019
# print("%d" % year)
# print("%0d" % year)
# print("%02d" % year)
# # %f默认会补0
# price = 108.9052
# # %f默认会补0，小数点后满足6位
# print("price= %f" % price)
# # %.1f .1 表示小数点后的位数为1，会取小数点后1位数，截取，不会四舍五入
# print("price= %.1f" % price)
# # %.f 会向上取整 108.9显示109
# print("price= %.f" % price)
# # %.0f （同上）会向上取整 108.9显示109
# print("price= %.f" % price)
#
# #format 格式化
# print("乔治说他今年{}岁了".format(age))
# school = "红黄蓝"
# print("乔治说他今年{}岁了，在{}幼儿园上学".format(age,school))
# # str = input("请输入：")
# # print("str="+str)
# print(int(10.6))
# # id 获取内存地址
# print(id("aaa"))
# num_1 = 4
# print(id(num_1))
# num_1+=2
# print(id(num_1))
#
# print(1.23e5)
#
# print(False or True)
# # 三个除法的运算符
# print(10/3)
# # 小数点之后会保存一位，结果为 3.0
# print(9/3)
# print(10//3)
# print(10%3)
#
# print('%2d' % 3000)
# print('%02d' % 3.0)
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# s1 = 72
# s2 = 85
# r = (85-72)/72*100
# print(r)
# print('%0.1f %%' % r)
#
# arr = ["aaa","bbb","ccc"]
# print(arr)
#
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(len(arr))
# str = "werw"
# print(str[0])
# print(len(str))

# age= 11
# if age>50:
#     print("中年人")
# elif age>18:
#     print("青年人")
# elif age>10:
#     print("少儿")
# else:
#     print("儿童")

sum = 0
ll = range(4)
for a in ll :
    sum+=a
print(sum)