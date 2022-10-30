# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(self.name+'在吃饭')

# xbai = Student('张三',20)
# xhei = Student('李四',200)
# xbai.eat()
# xhei.eat()
# # print(id(xbai))
# # print(id(xhei))
# # 为某实例动态绑定性别属性
# xhei.gender = '男'
# print('小黑的动态绑定的属性： ',xhei.gender)

# def show():
#     print('定义在类之外的，称为函数')

# xbai.show=show 
# xbai.show()
# # xhei.show()


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         # 年龄不希望在类的外部被使用，所以这种写法
#         self.__age = age
#     def show(self):
#         print(self.name,self.__age)

# xbai = Student('张三',20)
# xbai.show()
# # 在类的外部使用 name 与 age
# print(xbai.name)
# # print(xbai.__age)
# # print(dir(xbai))
# # print(xbai._Student__age)  # 在类的外部可以使用这种方式进行访问到。但是不推荐。。


from importlib.resources import Package
from re import A
import sched
from time import time
from unicodedata import name

# # Person 继承于 object
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(self.name,self.age)

# class Student(Person):
#     def __init__(self,name,age,stu_num):
#         super().__init__(name,age)
#         self.stu_num = stu_num

#     # 对 info 方法重写
#     # 这样，学生不仅输出info() 的内容，还有 stu_name
#     def info(self):
#         super().info()
#         print(self.stu_num)
# class Teacher(Person):
#     def __init__(self,name,age,teachYear):
#         super().__init__(name,age)
#         self.teachYear = teachYear
#     def info(self):
#         super().info()
#         print('教龄为： ',self.teachYear)

# xbai = Student('张三',20,'1001')
# xhei = Teacher('李四',10,10)
# xbai.info()
# print('=='*6)
# xhei.info()
# # print('学生姓名： {0}\n学生年龄： {1}\n学生学号： {2}'.format(xbai.name,xbai.age,xbai.stu_num))




# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return '我的名字是： {0}，今年{1}岁'.format(self.name,self.age)

# xbai = Student('张三',20)
# print(dir(xbai))
# print(xbai)
# print(type(xbai))

# print('多态'.center(20,'='))
# # 不写，则默认继承于 object, object 是所有类的父类
# class Animal:
#     def eat(self):
#         print('动物会吃')
# class Dog(Animal):
#     # 对 eat 方法重写
#     def eat(self):
#         print('狗吃骨头')
# class Cat(Animal):
#     def eat(self):
#         print('猫吃鱼')
# class Person:
#     def eat(self):
#         print('人吃五谷杂粮')
# # 定义一个函数
# def fun(obj):
#     obj.eat()

# fun(Cat())
# fun(Dog())
# fun(Animal())
# # Person 不继承 Animal，但是有 eat 方法。
# # 动态语言的多态崇尚“鸭子类型”。 不需关心对象是什么类型（是不是鸭子），只关心对象的行为
# fun(Person())


# title="特殊方法和特殊属性"
# print(title.center(50,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["特殊属性","__dict__","获得类对象或实例对象所绑定的所有属性和方法的字典"],
#     ["特殊方法","__len__()","通过重写该方法，让内置函数 len() 的参数可以是自定义类型"],
#     ["特殊方法","__add__()","通过重写该方法，可使用自定义对象具有“+” 功能"],
#     ["特殊方法","__new__()","用于创建对象"],
#     ["特殊方法","__init__()","对创建的对象进行初始化"]
#     ]

# d_headers = headers=["", "名称", "描述"]
# print(tabulate(d,d_headers,tablefmt='grid'))


# class Student:
#     def __init__(sf,name):
#         sf.name = name
#     def __add__(sf,oer):
#         return sf.name + oer.name
#     def __len__(sf):
#         return len(sf.name) 
# xbai = Student('Jack')
# xhei = Student('李四')
# # 实现了两个对象的加法运算（因为在 Student 类中，重写了 __add__()）
# x = xbai + xhei
# # print(x)
# # print(xbai.__add__(xhei))

# lst = [11,22,33,44]
# print(len(lst))
# print(lst.__len__())
# print('对象',xbai.name,'的长度： ',len(xbai))

# print('\n\n\n\n')
# class Person:
#     def __new__(cls,*args,**kwargs):
#         print('__new__ 被调用执行了，cls 的id 值为{0}'.format(id(cls)))
#         obj = super().__new__(cls)
#         print('创建的对象的id 为： {0}'.format(id(obj)))
#         return obj
#         # obj 的值，返回给到 sf

#     def __init__(sf,name,age):
#         print('__init__ 被调用了，self 的id 值为： {0}'.format(sf))
#         sf.name = name
#         sf.age = age

# print('object 这个类对象的id 为： {0}'.format(id(object)))
# print('Person 这个类对象的id 为： {0}'.format(id(Person)))
# # 创建 Person 类的实例对象
# q = Person('张三',20)
# print('q 这个 Person 类的实例对象的id 为： {0}'.format(id(q)))


# class Cpu:
#     pass
# class Disk:
#     pass
# class Computer:
#     def __init__(sf,cpu,disk):
#         sf.cpu = cpu
#         sf.disk = disk
# # 变量的赋值
# cpu1 = Cpu()
# cpu2 = cpu1
# # 实际上，一个对象放到两个变量中进行存储
# print(cpu1)
# print(cpu2)
# print('类的浅拷贝'.center(30,'='))
# # 浅拷贝，Python 一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝。
# # 因此源对象与拷贝对象会引用同一个子对象
# disk1 = Disk()
# compu1 = Computer(cpu1,disk1)
# # 深拷贝。使用 copy 模块的 deepcopy 函数，递归拷贝对象中包含的子对象，
# # 源对象和拷贝对象所有的子对象也不相同
# import copy
# print(disk1)
# compu2 = copy.copy(compu1)
# print(compu1,compu1.cpu,compu1.disk)
# print(compu2,compu2.cpu,compu2.disk)


# # import calc
# # print(calc.add(10,20))
# # print(calc.div(10,20))
# # 第二种方法
# from calc import add
# print(add(10,20)) 

# # 在模块中导入 package 包
# import packages.module_a as ma  # ma 是 packages.module_a 这个模块的别名
# print(ma.a)


# title="python 中常用的内置模块"
# print(title.center(50,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["sys","与Python 解释器及其环境操作相关的标准库"],
#     ["time","提供与事件相关的各种函数的标准库"],
#     ["os","提供了访问操作系统服务功能的标准库"],
#     ["calendar","提供与日期相关的各种函数的标准库"],
#     ["urllib","用于读取来自网上（服务器）的数据标准库"],
#     ["json","用于使用 JSON 序列化和反序列化对象"],
#     ["re","用于在字符串中执行正则表达式匹配和替换"],
#     ["math","提供标准算术运算函数的标准库"],
#     ["decimal","用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算"],
#     ["logging","提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能"]
#     ]

# d_headers = headers=["模块名", "描述"]
# print(tabulate(d,d_headers,tablefmt='grid'))


# import sys, time, os ,calendar, urllib, json, re, math, decimal, logging
# import urllib.request
# print(sys.getsizeof(24))
# print(sys.getsizeof(True))
# print(time.time())
# print(time.localtime(time.time()))
# # print(urllib.request.urlopen('https://www.baidu.com').read())
# print(math.pi)


# import schedule, time
# # 定时任务，，定时发送邮件类似的
# def job():
#     print('haha------q')

# schedule.every(3).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)








