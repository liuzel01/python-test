'''1. 编码格式介绍
2. 文件的读写原理
3. 文件读写操作
4. 文件对象常用的方法
5. with 语句（上下文管理器）
6. 目录操作
'''

# Python 的解释器使用 Unicode（内存）
# .py 文件在磁盘上使用 UTF-8 存储（外存）

# encoding gbk
# print('你好，中国')
# 读取磁盘文件的内容
# file = open('a.txt','r')
# print(file.readlines())
# file.close()

# f = open('b.txt','a')
# f.write('Python\n')
# f.close()

# # 复制图片，b 以二进制方式打开文件
# src_file = open('logo.jpg','rb')
# target_file = open('copylogo.png','wb')
# target_file.write(src_file.read())
# target_file.close()
# src_file.close()

# file = open('a.txt','a')
# # print(file.read(2))
# # print(file.readline())
# # print(file.readlines())
# lst = ['java','go','python']
# file.writelines(lst)
# file.close()

# file = open('a.txt','r')
# file.seek(0)
# print(file.read())
# # 返回文件指针的当前位置
# print(file.tell())
# file.close()

# with 语句自动管理上下文资源，不论什么原因跳出 with 的都能确保文件正确关闭，以此达到释放资源的目的
# with open('a.txt', 'r') as f:
#     print(f.read())
# # 无论程序是否异常，都会调用 exit
# class MyContentMgr:
#     def __enter__(sf):
#         print("Enter 方法被调用执行了")
#         return sf
#     def __exit__(sf,exec_type,exec_val,exec_tb):
#         print('exit 方法被调用执行了')
#     def show(sf):
#         print('show 方法被调用执行了',1 / 0)
# with MyContentMgr() as f:  # 相当于 file = MyContentMgr()
#     f.show()
    
# with open('logo.jpg','rb') as src_file:
#     with open('copy2logo.png','wb') as target_file:
#         target_file.write(src_file.read())


# title="python 中常用的内置模块"
# print(title.center(65,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["getcwd()","返回当前的工作目录"],
#     ["listdir(path)","返回指定路径下的文件和目录信息"],
#     ["mkdir(path[,mode])","创建目录"],
#     ["makedirs(path1/path2...[,mode])","创建多级目录"],
#     ["rmdir(path)","删除目录"],
#     ["removedirs(path1/path2...)","删除多级目录"],
#     ["chdir(path)","将 path 设置为当前工作目录"]
#     ]

# d_headers = headers=["函数", "说明"]
# print(tabulate(d,d_headers,tablefmt='grid'))

# import os
# 调用操作系统的程序、可执行文件（下面示例是windows的，）
# os.system('notepad')
# os.system('calc.exe')
# print(os.getcwd())
# print(os.listdir('../chart'))
# os.mkdir('newdir2')
# os.rmdir('newdir2')
# os.makedirs('a/b/c')
# os.removedirs('a/b/c')
# os.chdir('/home/devops/dl.lng/')
# print(os.getcwd())


# title="os.path 模块操作目录相关函数"
# print(title.center(65,'='))
# from tabulate import tabulate
# import wcwidth

# d = [
#     ["abspath(path)","用于获取文件或目录的绝对路径"],
#     ["exists(path)","用于判断文件或目录是否存在，如果存在返回True，\n否则返回False"],
#     ["join(path,name)","将目录与目录或者文件名拼接起来"],
#     ["splitext()","分离文件名和扩展名"],
#     ["basename(path)","从一个目录中提取文件名"],
#     ["dirname(path)","从一个路径中提取文件路径，不包括文件名"],
#     ["isdir(path)","用于判断是否为路径"]
#     ]

# d_headers = headers=["函数", "说明"]
# print(tabulate(d,d_headers,tablefmt='grid'))

# print(os.path.abspath('demo.py'))
# print(os.path.exists('demo.py'),os.path.exists('demo18.pyc'))
# print(os.path.join('/root/gitlab-python/l01','demo-object.py'))
# print(os.path.split('/root/gitlab-python/l01/demo-object.py'))
# print(os.path.splitext('demo-object.py'))
# print(os.path.basename('/root/gitlab-python/l01/demo-object.py'))
# print(os.path.dirname('/root/gitlab-python/l01/demo-object.py'))
# print(os.path.isdir('/root/gitlab-python/l01/demo-object.py'))


# 列出指定目录下的所有 py 文件
# 对结果进行 批量的处理
# import os
# ph = os.getcwd()
# lst = os.listdir(ph)
# for f in lst:
#     if f.endswith('.py'):
#         print(f)

import os
ph = os.getcwd()
lst_f = os.walk(ph)
# print(lst_f)
for dirph,dirname,fname in lst_f:
    # print(dirph)
    # print(dirname)
    # print(fname)
    # print('=='*20)
    for dir in dirname:
        # 打印出，当前目录下的所有目录
        print(os.path.join(dirph,dir))
    for f in fname:
        print(os.path.join(dirph,f))
    print('=='*20)
        
        





















