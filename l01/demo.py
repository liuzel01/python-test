from imaplib import Int2AP
from operator import contains
from ssl import SSLWantReadError


name = '玛丽亚'
age = 76

# print(type(name),type(age))
# print('我叫'+ name +'，今年'+ str(age) +'岁')
# print('------------------str() 将其他类型转成 str 类型---')

a = 10
b = 198.8
c = False
# print(type(a),type(b),type(c))
# print("""str(a),str(b),str(c),
# type(str(a)),type(str(b)),type(str(c))
# """)
# print('------------------int() 将其他类型转成 int 类型---')
s1 = '123'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
# print (type(s1),type(f1),type(s2),type(ff),type(s3))
# print (int(s1),type(int(s1)))
# print (int(s1),type(int(s1)))
# # print (int(s2),type(int(s2)))     # str 转成 int 报错，因为字符春为小数串
# print (int(ff),type(int(ff)))
# # print (int(s3),type(int(s3)))     # str 转成 int 类型时，字符串必须为数字串（整数）

# print('------------------float() 将其他类型转成 float 类型---')
s1 = '128.98'
s2 = '76'
ff = True
s3 = 'hello'
i = 98
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

print('输出 100 到 999 之间的水仙花数')
for i in range(100,1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    # print(bai,shi,ge)
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)