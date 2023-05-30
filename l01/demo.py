# coding=utf-8
import random
from ast import Num, arg
from imaplib import Int2AP
from inspect import trace
from operator import contains, ge, index
# from ossaudiodev import SNDCTL_COPR_RCODE
from re import L
from ssl import SSLWantReadError
# from symbol import factor
from textwrap import indent
from tkinter import CENTER
from traceback import print_last
import traceback
from unittest import result
from webbrowser import get

from pyparsing import null_debug_action

'''注释写法： 
单行一个 # ，
vscode 快捷键： Ctrl + /


'''
# --------------------------------------------------------
# name = '玛丽亚'
# age = 76

# print(type(name),type(age))
# print('我叫'+ name +'，今年'+ str(age) +'岁')
# print('------------------str() 将其他类型转成 str 类型---')

# a = 10
# b = 198.8
# c = False
# print(type(a),type(b),type(c))
# print("""str(a),str(b),str(c),
# type(str(a)),type(str(b)),type(str(c))
# """)
# print('------------------int() 将其他类型转成 int 类型---')
# s1 = '123'
# f1 = 98.7
# s2 = '76.77'
# ff = True
# s3 = 'hello'
# print (type(s1),type(f1),type(s2),type(ff),type(s3))
# print (int(s1),type(int(s1)))
# print (int(s1),type(int(s1)))
# # print (int(s2),type(int(s2)))     # str 转成 int 报错，因为字符春为小数串
# print (int(ff),type(int(ff)))
# # print (int(s3),type(int(s3)))     # str 转成 int 类型时，字符串必须为数字串（整数）

# print('------------------float() 将其他类型转成 float 类型---')
# s1 = '128.98'
# s2 = '76'
# ff = True
# s3 = 'hello'
# i = 98
'''print (type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
# print(float(s3),type(float(s3)))      # 字符串中的数字如果是非数字串，则不允许转换
print(float(i),type(float(i)))'''

# present = input('大声想要什么礼物: \n')
# print(present,type(present))

# a = int(input('请输入一个加数： '))
# b = int(input('请输入另一个加数： '))
# print(a+b)

# print(11/2)     # 除法运算
# print(11//2)    # 整除运算
# print(11%2)     # 取余
# print(9//-4)    
# print(-9//4)    # 一正一负的整数公式，向下取整
# print(9%-4)     # 取余公式： 余数=被除数-除数*商
# print(-9%4)

# a = 20
# a -=30
# print(a)
# a *= 19
# print(a)
# a /= 2
# print(a,type(a))
# a //= 2
# print(a)
# a %= 3
# print(a)
# print('------------------交换两个变量的值---')
# a,b = 10,20
# print('交换之前： ',a,b)
# a,b = b,a
# print('交换之后： ',a,b)
# print('------------------比较运算符---')
# a,b = 10,20
# c = 10
# print('a>b 吗？ ',a>b)
# print('a<b 吗？ ',a<b)
# print('a==b 吗？ ',a==b)
# print('a!=b 吗？ ',a!=b)
# print(a==c)
# print(a is c)       # 对象 id 的比较 
# print(a==10 and b==c)

# print('------------------not 对 bool 类型操作数取反---')
# f = True
# f2 = False
# print(not f)
# print(not f2)

# print('------------------in 与not in---')
# s = 'helloworld'
# print('w' in s)
# print('w' not in s)

# print('------------------程序开始---')
# print('1. 把冰箱门打开')
# print('2. 把大象放冰箱里')
# print('3. 把冰箱门关上')
# print('------------------程序结束---')

# print('------------------以下对象的 bool 值为 False，其他对象的均为 True---')
# print(bool(False))
# print(bool(0))
# print(bool(0.0))
# print(bool([]))     # 空列表
# print(bool(list()))
# print(bool(()))     # 空元组
# print(bool(tuple()))
# print(bool({}))     # 空字典
# print(bool(dict()))
# print(bool(set()))      # 空集合

# num = int(input('请输入一个整数： '))
# if num%2 == 0:
#     print(num,' 是偶数')
# else:
#     print(num,' 是奇数')

# num = int(input('请输入一个成绩： '))
# if 90 <= num < 100:
#     print(num,' A')
# elif 80 <= num < 89:
#     print(num,' B')
# elif 70 <= num < 79:
#     print(num,' C')
# elif 60 <= num < 69:
#     print(num,' D')
# elif 0 <= num < 59:
#     print(num,' E')
# else:
#     print('非法数据！不是成绩的有效成绩')

# a = int(input('请输入第一个整数： '))
# b = int(input('请输入第二个整数： '))
# print('使用条件表达式进入比较')
# print(
# #     (a,'大于等于',b) if a >= b else (b,'大于',a)
#     str(a)+' 大于等于 '+str(b) if a >= b else str(b)+' 大于 '+str(a)
# )

# print('pass 语句，什么都不做，只是一个占位符，用到需要写语句的地方')

# # range() 的三种创建方式
# r = range(10)
# print(r)
# print(list(r))
# r = range(1,11)       # 输出从1 到 10 的序列，步长为 1
# print(r)
# print(list(r))
# r = range(1,12,2)     # 输出从1 到 11 的序列，步长为 2
# print(r)
# print(list(r))
# print(10 in r)

# sum = 0
# a = 0
# while a < 5:
#     print(a < 5)
#     sum += a
#     print('sum: ',sum)
#     a += 1
#     print('a: ',a)
# print('和为： ',sum)

# sum = 0
# i = 1
# while i <= 100:
#     if not i % 2 :
#         sum += i
# #     sum += i if bool(i % 2)       这句有个错误！！！！！！！
#     i += 1
# print('1-100 之间的偶数和为： ',sum)

# for i in range(10):
#     print(i)
# for _ in range(5):
#     print('我用 python')

# print('使用 for 循环计算1 到 100 的偶数和')
# sum = 0
# for i in range(1,101):
#     if not i % 2:
#         sum += i
# print('1-100 的偶数和为： ',sum)

# print('输出 100 到 999 之间的水仙花数')
# for i in range(100,1000):
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     # print(bai,shi,ge)
#     if ge ** 3 + shi ** 3 + bai ** 3 == i:
#         print(i)

# 从键盘录入密码，最多录入 3 次，如果正确就结束循环

# for i in range(3):
#     pwd = input('请输入密码： ')
#     if pwd == '8888':
#         print('密码正确')
#         break
#     else: 
#         print('密码不正确')
# while 写法
# a = 0
# while a < 3:
#     pwd = input('请输入密码： ')
#     a += 1
#     if pwd == '8888':
#         print('密码正确')
#         break
#     else: 
#         print('密码不正确')
# else:
#     print('三次密码均输入错误')

# 输出 1-50 所有 5 的倍数，
# for i in range(1,51):
#     if i % 5 == 0:
#         print(i,' 为 5 的倍数')
# # continue
# for i in range(1,51):
#     if i % 5 != 0:
#         continue
#     else:
#         print(i,' 为 5 的倍数')

'''输入一个三行四列的矩形'''
# for i in range(3):
#     for j in range(4):
#         print('*',end='\t')     # 不换行输出
#     print()     # 换行

# for i in range(1,10):
# #     print(i)
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end='\t')
#     print()s

# for i in range(5):
#     for j in range(1,11):
#         if j % 2 == 0:
#             continue
#         print(j,end='\t')
#     print()

'''创建列表'''
# lst = ['hello','world',98,'hello',234]      # 获取单个元素。正向索引： 从 0 到 N-1，逆向索引： 从 -N 到 -1 
# print(lst)
# print(lst.index('hello'))       # 列表中有相同元素，只返回列表中相同元素的第一个元素的索引
# # print(lst.index('hello',1,3))       # 在 index 为1，2(不包括右边3) 中去查找字符串 'hello'，查不到所以抛出异常
# print(lst[2])
# print(lst[-3])

# lst = [10,20,30,40,50,60,70,80,90,90,90]
# # print(lst[1:6:])     # 切片，索引 1 到 5 的部分，步长为 1 
# print(lst[1:6:2])
# print(lst[:6:2])        # 默认开始，从索引为 0 开始
# print(lst[1::2])        # 默认结束，到最后
# print(lst[::-1])

# # 列表元素添加操作
# lst = [10,20,30,40]
# # print(10 in lst)
# ls2=['hello','world']
# ls3=[True,False,'hello']
# # lst.append(ls2)
# # print(lst)
# # lst.extend(ls2)
# # print(lst)
# # 在任意位置上添加一个元素
# lst.insert(1,90)
# # print(lst)
# lst[1:]=ls3
# print(lst)

# # 列表元素删除操作
# lst = [10,20,30,40,60,30]
# # lst.remove(30)
# print(lst)
# lst.pop(1)
# print(lst)
# lst.pop(1)
# print(lst)
# qq=lst.pop()
# print(qq)
# lst[1:3]=[]
# print(lst)

# 字典 dict
# scores={'张三':100,'里斯':200,'王五':45}
# print(scores)
# print(type(scores))
# stu=dict(name='jack',age=20)
# print(stu)

# 获取字典元素
# print(scores['张三'])
# # print(scores['chenliu'])
# print(scores.get('张三'))
# # get 方法不会报错。。
# print(scores.get('chenliu'))
# # 99看作 key 不存在时的默认值
# print(scores.get('玛奇',99))

# key 的判断
# print('三' in scores)
# 删除键值
# del scores['张三']
# print(scores)
# scores.clear()
# 新增、修改
# scores['chenliu']=998
# # print(scores)
# scores['里斯']=302
# print(scores)
# print(scores.keys())
# print('转换成 list： ',list(scores.keys()))
# # print(type(scores.keys()))
# print(scores.values())
# print('转换成 list： ',list(scores.values()))
# print(scores.items())
# # 转换后的列表元素，是由元组组成
# print('转换成 list： ',list(scores.items()))
# for i in scores:
#     print(i,scores.get(i))

# 字典生成式
# i = ['Fruits','Bookds','Others']
# price = [96,78,86,100,110]
# d={i.upper():price for i,price in zip(i,price)}
# print(d)

# lst=[10,20,45]
# print(id(lst))
# print(id(lst.append(300)))
# lst.append(300)
# print(lst)
# print(id(lst))

# # 元组创建方式，不可变序列
# t=('Python','world',98)
# print(t)
# print(type(t))
# t1='Python','world',98
# print(type(t1))
# # 只有一个元素，需要加(,)
# t1=('python',)
# print(t1)
# print(type(t1))
# # 空元组创建
# t2=()
# print('空元组',t2,type(t2))
# print('空字典',{})
# print('空列表',[])

# 集合创建方式，是无序的
# 元素不允许重复
# s={2,3,4,5,6,7,7,8,}
# print(s)
# s1=set(range(6))
# s2=set([1,2,3,4,5,5,6,6])
# s3=set((1,2,3,4,4,5,5,66))
# print(s1,type(s1))
# print(s2,type(s2))
# print(s3,type(s3))
# print(set('Python'))
# print(set())

# s = {10,2,3,4,5}
# print(s)
# # s.add(80)
# print(s)
# # 一次至少添加一个
# s.update({80,80,90,110})
# # print(s)
# s.update([66666])
# # print(s)
# s.update((87,98,76))
# print(s)
# # s.remove(10)
# s.discard(5050505)
# print(s)
# s.pop()
# print(s)
# 集合之间的关系
# s1={1,2,3,4,5}
# s2={1,2,4,5,3,6,8,9}
# s3={6,20,222,333}
# # print(s1==s2)
# # print(s1.issubset(s2))
# # print(s2.issuperset(s1))
# # print(s1.isdisjoint(s3))
# # print(s2.isdisjoint(s3))
# # 交集操作
# print(s1.intersection(s2))
# print(s1 & s2)
# print(s1.union(s3))
# print(s1 | s3)
# print(s1,s3)
# # 差集
# print(s2.difference(s1))
# print(s1.difference(s3))
# print(s3 - s2)
# # 对称差集
# print(s1.symmetric_difference(s2))
# print(s3.symmetric_difference(s2))
# print(s3.symmetric_difference(s1))

# 集合生成式
# s={ i*i for i in range(6) }
# print(s)

# title="列表、字典、元组、集合总结"
# print(title.center(70,'='))

# from tabulate import tabulate
# import wcwidth

# d = [
#     ["列表（list）","可变","可重复","有序","[]"],
#     ["元组（tuple）","不可变","可重复","有序","()"],
#     ["字典（dict）","可变","key可重复 \nvalue可重复","无序","{key:value}"],
#     ["集合（set）","可变","不可重复","无序","{}"]
#     ]

# d_headers = headers=["数据结构", "是否可变", "是否重复","是否有序","定义符号"]
# print(tabulate(d,d_headers,tablefmt='grid'))

# 字符串驻留机制
# a='Python'
# b="Python"
# c='''Python'''
# print(id(a))
# print(id(b))
# print(id(c))
# 转成大写后，会产生一个新的字符串对象
# s=a.upper()
# s2=a.lower()
# print(a,id(a))
# print(s,id(s))
# print(s2,id(s2))
# print(s.title())
# print(a.center(50,'*'))
# print(a.ljust(20,'*'))
# print(a.rjust(20))
# print(a.zfill(20))
# print('-8910'.zfill(8))

# 字符串劈分操作的方法
# a='hello python world'
# print(a.split())
# print(a.split(maxsplit=1))
# print(a.split(sep='o',maxsplit=2))
# print('='*30)
# print(a.rsplit())
# print(a.rsplit(maxsplit=1))
# print(a.rsplit(sep='o',maxsplit=2))

# 字符串常用操作
# 是否是有效标识符
# print('1. ',a.isidentifier())
# print('2. ','hello'.isidentifier())
# print('3. ','张三_'.isidentifier())
# print('4. ','张三_2'.isidentifier())
# print('5. ','\t'.isspace())
# print('6. ',a.isalpha())
# print('7. ','123'.isdecimal())
# print('8. ','123四'.isdecimal())
# print('9. ','123四'.isnumeric())
# print('10. ','张三123'.isalnum())
# print('10. ','abc!'.isalnum())

# print(a.replace('o','java',2))
# print(a[-7:-13:-1])
# print(a[6:13:])

# name='张三'
# age=20
# print('我叫 %s ，今年 %d 岁'%(name,age))
# print('我叫 {0} ，今年 {1} 岁'.format(name,age))
# print(f'我叫 {name} ，今年 {age} 岁')

# print('%10d',)
print('上面有待补充','=='*20)

# def cale(a,b):
#     c = a + b 
#     return c
# # 位置实参
# result=cale(10,20)
# print(result)
# # res 关键字参数
# print('res: ',cale(b=10,a=20))

# def fun(ar1,ar2):
#     print('ar1: ',ar1)
#     print('ar2: ',ar2)
#     ar1 = 100
#     ar2.append(200)
#     print('ar1: ',ar1)
#     print('ar2: ',ar2)
# q = 11
# w = [22,33,11]
# # q, w 是调用处的实参，ar1, ar2 是定义处的形参
# fun(q,w)
# print('q: ',q)
# print('w: ',w)
'''在函数调用过程中，进行参数的传递。
如果是不可变对象，在函数体的修改不会影响实参的值，
如果是不可变对象，则会影响到实参的值'''

# print(bool(0))
# print(bool(8))
# def fun(num):
#     odd = []
#     even = []
#     for i in num:
#         if i % 2:
#             odd.append(i)
#         else:
#             even.append(i)
#     return odd,even
# lst = [10,29,34,23,44,53,55]
# print(fun(lst))

'''函数的返回值，
如果没有返回值（fun 执行完毕后，不需要给调用处提供数据），return 可以忽略不写
fun 返回值是1个，直接返回类型
fun 返回值是多个，返回的结果为元组'''

# def fun(a,b=10):
#     print(a,b)
# fun(100)

# 可变的位置参数
# def fun(*args):
#     print(args)
#     # print(args[0])
# fun(10)
# fun(10,20)
# fun(30,405,60)

# 定义个数可变的关键字形参，结果是字典
# def fun(**args):
#     print(args)
# fun(a=10)
# fun(a=10,b=20,c=30)

# def fun2(*args,*a):
#     pass
# 以上代码，程序会报错，可变的位置参数，只能是1个
# 以上代码，程序会报错，可变的关键字参数，只能是1个

# def fun3(**arg1,*arg2):
#     pass
# 函数定义，既有个数可变的关键字形参，也有个数可变的位置形参，后者应该放前面


# title="函数的参数总结"
# print(title.center(75,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["位置实参","","√",""],
#     ["将序列中的每个元素都转换为位置实参","","√","使用*"],
#     ["关键字实参","","√",""],
#     ["将字典中的每个键值对都转换为关键字实参","","√","使用**"],
#     ["默认值形参","√","",""],
#     ["关键字形参","√","","使用*"],
#     ["个数可变的位置形参","√","","使用*"],
#     ["个数可变的关键字形参","√","","使用**"]
#     ]

# d_headers = headers=["参数的类型", "函数的定义", "函数的调用","备注"]
# print(tabulate(d,d_headers,tablefmt='grid'))

# def fun(a,b,c):
#     print('a= ',a)
#     print('b= ',b)
#     print('c= ',c)
# fun(10,20,30)

# lst=[11,22,33]
# # fun(*lst)
# # fun(a=100,b=200,c=300)
# dic={'a':111,'b':222,'c':333}
# fun(**dic)

# 从* 之后的参数，在函数调用时只能采用关键字参数传递
# def fun4(a,b,*,c,d):
#     print('a= ',a)
#     print('b= ',b)
#     print('c= ',c)
#     print('d= ',d)
# # 关键字实参传递
# fun4(a=10,b=20,c=30,d=40)
# # 前两个参数，使用位置实参传递；c和d使用关键字实参传递
# fun4(10,20,c=30,d=40)

# def fun5(a,b,*,c,d,**args):
#     pass
# def fun6(*args,**args2):
#     pass
# def fun7(a,b=10,*args,**args2):
#     pass

# 局部变量使用 global 声明，变成全局变量
# def fun():
#     global age
#     age = 20
#     print(age)
# fun()
# print(age)

# # 函数的递归函数（嵌套）
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         res = n * fac(n-1)
#         return res
#         # return n * fac(n-1)

# print(fac(6))

# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# # 斐波拉契第6位的数字
# print(fib(6))

# for n in range(1,7):
#     print(fib(n),end='\t')

# 异常处理
# try: 
#     a = int(input('输入第一个整数'))
#     b = int(input('输入第二个整数'))
#     res = a / b
#     print('结果为： ',res)
# except ZeroDivisionError:
#     print('除数不允许为0')
# except ValueError:
#     print('只允许输入数字串')

# print('完成计算')

# # 另一种方式
# try: 
#     a = int(input('输入第一个整数'))
#     b = int(input('输入第二个整数'))
#     res = a / b
# except BaseException as e:
#     print('报错信息： ',e)
# else:
#     print('计算结果为： ',res)

# # 另一种方式
# try: 
#     a = int(input('输入第一个整数'))
#     b = int(input('输入第二个整数'))
#     res = a / b
# except BaseException as e:
#     print('报错信息： ',e)
# else:
#     print('计算结果为： ',res)
# finally:
#     print('谢谢使用')


# title="python常见的异常类型"
# print(title.center(50,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["ZeroDivisionError","除（或取模）零（所有数据类型）"],
#     ["IndexError","序列中没有此索引（index）"],
#     ["KeyError","映射中没有这个键"],
#     ["NameError","未声明/初始化对象（没有属性）"],
#     ["SyntaxError","Python语法错误"],
#     ["ValueError","传入无效的参数"]
#     ]

# d_headers = headers=["异常类型", "描述", "函数的调用","备注"]
# print(tabulate(d,d_headers,tablefmt='grid'))

# import traceback
# try:
#     print('-----')
#     print(1/0)
# except:
#     traceback.print_exc()


# title="python常见的异常类型"
# print(title.center(50,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["ZeroDivisionError","除（或取模）零（所有数据类型）"],
#     ["IndexError","序列中没有此索引（index）"],
#     ["KeyError","映射中没有这个键"],
#     ["NameError","未声明/初始化对象（没有属性）"],
#     ["SyntaxError","Python语法错误"],
#     ["ValueError","传入无效的参数"]
#     ]

# d_headers = headers=["异常类型", "描述", "函数的调用","备注"]
# print(tabulate(d,d_headers,tablefmt='grid'))


# print('Python 中一切皆对象'.center(70,'='))
# print('hello world!')

# Student 为类的名称（类名），由一个或多个单词组成，单个单词的首字母大写，其余小写
# Student 也是对象，内存也有开空间
class Student:
    # 直接写在类里的变量，称为类属性
    native_place = '吉林'  
    # 初始化方法
    def __init__(self,name,age):
        # self.name 成为实体属性，进行了赋值操作，将局部变量的 name 的值赋给实体属性
        self.name = name
        self.age = age
# 实例方法
# 在类之外定义的称为函数，类之内定义的称为方法
    def eat(selflflflf):
        print('学生在吃饭。。')
# 静态方法
# 没有任何默认的参数
    @staticmethod
    def method():
        print('使用了 staticmethod 进行修饰，所以是静态方法')
# 类方法
    @classmethod
    def cm(clsssss):
        print('使用了 classmethod 进行修饰，所以是类方法')

# xbai=Student('张三',20)
# # xbai 是 Student 类的一个实例对象
# # 一个 Student 类可以创建N 多个 Student 类的实例对象，每个实例对象的属性值可同可不同
# print(xbai.age)
# print(xbai.native_place)
# xbai.eat()
# Student.eat(xbai)   # 同样是调用 Seudent 中的 eat 方法
#                     # 类名.方法名(类的对象)， 实际上就是方法定义出的 self


# # 类属性： 类中方法外的属性称为类属性。被该类的所有对象所共享
# xbai = Student('张三',20)
# xhei = Student('李四',10)
# print(xbai.native_place)
# print(xhei.native_place)
# print(xbai.name)
# xbai.name = '张三三'
# print(xbai.name)
# # 类方法的调用，使用类名直接访问
# Student.cm()
# # 静态方法的调用，使用类型直接访问
# Student.method()

# name = 'liuzelin'
# age = 22
# weight = 75.5
# stu_id = 25
# 解决数据对齐显示
# print('我的学号是： %03d'%stu_id)
# # print(f'我的名字是： %s，今年 %s 岁了，体重 %s 公斤'%(name,age,weight))
# print(f'我的名字是： {name}，今年 {age} 岁了，体重 {weight} 公斤')

# str2 = '1.1'
# str3 = '(1,2,3)'
# str4 = '[1,2,3,4]'
# # eval 用来计算在字符串中的有效 python 表达式，并返回一个对象值
# print(eval(str2))
# print(eval(str3))
# print(eval(str4))

# player = int(input('请出拳（0--石头；1--剪刀；2-布）： '))
# computer = random.randint(0,2)
# if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
#     print('玩家获胜')
# elif (player == computer):
#     print('平局')
# else:
#     print('电脑获胜')
# print('游戏结束')

# # 三目运算符
# aa,bb = 10,60
# cc = aa - bb if aa > bb else bb - aa
# print(cc)

# 1..100 以内的数字求和
# i = 0
# res = 0
# while i < 10:
#     i += 1
#     # print(f'当前 i 的值： {i}')
#     if i % 2 == 0:
#         # print(f'当前计算： result = {res} + {i}')
#         res += i
#         print(f'截至本次 res 的值： {res}')


# i = 1
# while i <= 5:
#     if i == 3:
#         print('吃出一个虫子，这个苹果不吃了')
#         i += 1
#         continue
#     print(f'吃了第{i}个苹果')
#     i += 1

# d = 0
# while d < 3:
#     print(f'第{d+1}天')
#     a = 0
#     # print(f'a的值为{a}')
#     while a < 3:
#         print('abcabc')
#         a += 1
#         # print(f'a的值为{a}')
#         # break
#     print('今天去刷碗。惩罚结束')
#     d += 1

# 打印矩形
# i = 1
# while i < 5:
#     i += 1
#     print('*'*i)
# while i < 5:
#     i += 1
#     j = 0
#     while j < i:
#         print('*',end='')
#         j += 1
#     print()

# j = 1
# while j <= 9:
#     # print(f'{j} * {i} = {j*i}',end='')
#     i = 1
#     while i <= j:
#         print(f'{i} * {j} = {j * i}',end='\t')
#         i += 1
#     print()
#     j += 1

abc = 'itheima'
for i in abc:
    print(i)










