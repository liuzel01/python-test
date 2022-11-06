# encoding: utf-8
'''1. 需求分析
    添加学生及成绩信息
    将学生信息保存到文件中
    修改/删除学生信息
    查询学生信息
    根据学生成绩进行排序
    统计学生总分
2. 系统设计
3. 系统开发必备
4. 主函数设计
5. 学生信息维护模块设计
6. 查询/统计模块设计
7. 排序模块设计
8. 项目打包'''

import os
from traceback import print_exc

fname = 'students.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择你要进行的操作： ').strip())
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                ans = input('此操作将退出系统，是否确认？ y/n')
                if ans == 'y' or ans == 'Y':
                    print('谢谢您的使用！！！')
                    # 退出系统
                    break
                else:
                    continue
            elif choice == 1:
                # 录入学生信息
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('学生信息管理系统'.center(50, '='))
    print('功能菜单'.center(55, '*'))
    print('\t\t1. 录入学生信息')
    print('\t\t2. 查找学生信息')
    print('\t\t3. 删除学生信息')
    print('\t\t4. 修改学生信息')
    print('\t\t5. 排序')
    print('\t\t6. 统计学生总人数')
    print('\t\t7. 显示所有学生信息')
    print('\t\t0. 退出系统')
    print('*'*55)


def insert():
    stu_lst = []
    while True:
        id = input('请输入 ID（如1001）： ').strip()
        if not id:
            break
        name = input('请输入姓名： ').strip()
        if not name:
            break
        try:
            english = int(input('请输入 英语 成绩： ').strip())
            python = int(input('请输入 python 成绩： ').strip())
            java = int(input('请输入 java 成绩： ').strip())
        except:
            print('所输入成绩无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典
        stu_info = {'id': id, 'name': name,
                    'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        stu_lst.append(stu_info)
        ans = input('是否继续添加？ y/n')
        if ans == 'y':
            continue
        else:
            break
    # 调用 save() 函数
    save(stu_lst)
    print('学生信息录入完毕！！！')


# 对文件进行操作，将录入信息保存到文件
def save(stu_lst):
    try:
        stu_txt = open(fname, 'a', encoding='utf-8')
    except:
        # 出现异常后的处理方式
        stu_txt = open(fname, 'w', encoding='utf-8')
    for i in stu_lst:
        # 将列表中每一项，转换成字符串
        stu_txt.write(str(i)+'\n')
    stu_txt.close()


def search():
    stu_query = []
    while 1:
        id = ''
        name = ''
        if os.path.exists(fname):
            mode = input('按 ID 查找请输入1，按姓名查找请输入2： ').strip()
            if mode == '1':
                id = input('请输入学生 ID： ').strip()
            elif mode == '2':
                name = input('请输入学生姓名： ').strip()
            else:
                print('您的输入有误，请重新输入！！！')
                search()
            with open(fname, 'r', encoding='utf-8') as rf:
                stu = rf.readlines()
                for i in stu:
                    d = dict(eval(i))
                    if id != '':
                        if d['id'] == id:
                            stu_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            stu_query.append(d)
            # 显示查询结果
            show_stu(stu_query)
            # 清空列表
            stu_query.clear()
            ans = input('是否继续查询？ y/n')
            if ans == 'y':
                continue
            else:
                # 退出循环
                break
        else:
            print('暂未保存学生信息')
            return


def show_stu(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        # 结束此方法
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'python 成绩', 'java 成绩', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for i in lst:
        print(format_data.format(i.get('id'),
                                 i.get('name'),
                                 i.get('english'),
                                 i.get('python'),
                                 i.get('java'),
                                 int(i.get('english')) +
                                 int(i.get('python'))+int(i.get('java'))
                                 ))


def delete():
    while 1:
        stu_id = input('请输入学生ID： ').strip()
        if stu_id != '':
            if os.path.exists(fname):
                with open(fname, 'r', encoding='utf-8') as f:
                    stu_old = f.readlines()
            else:
                stu_old = []
            # 标识是否删除
            flag = False
            if stu_old:
                with open(fname, 'w', encoding='utf-8') as fw:
                    d = {}
                    for i in stu_old:
                        # 将字符串转换成字典类型
                        d = dict(eval(i))
                        if d['id'] != stu_id:
                            fw.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'ID 为{stu_id}的学生信息已被删除')
                        # print('ID 为{stu_id}的学生信息已被删除'.format(stu_id=stu_id))
                    else:
                        print('没有找到ID为 {}的学生信息'.format(stu_id))
            else:
                # 列表中没有学生数据
                print('无学生信息！！！')
                break
            # 删除完后，展示所有学生信息
            show()
            # 判断是否继续该操作（选项），不继续则退出此选项
            ans = input('是否继续删除？ y/n')
            if ans == 'y':
                continue
            else:
                # 退出循环
                break


def modify():
    show()
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as rf:
            stu_old = rf.readlines()
    else:
        return
    stu_id = input('请输入要修改的学员的ID： ').strip()
    with open(fname, 'w', encoding='utf-8') as wf:
        for i in stu_old:
            d = dict(eval(i))
            if d['id'] == stu_id:
                print('找到这名学生了，可以修改他的相关信息了！ ')
                while True:
                    try:
                        d['name'] = input('请输入姓名： ').strip()
                        d['english'] = input('请输入英语成绩： ').strip()
                        d['python'] = input('请输入 python 成绩： ').strip()
                        d['java'] = input('请输入 java 成绩： ').strip()
                    except:
                        # 只要有错，就会重复上一步的 try
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wf.write(str(d) + '\n')
                print('修改成功！！')
            else:
                wf.write(str(d) + '\n')
            # 删除完后，展示所有学生信息
            # show()
            # 判断是否继续该操作（选项），不继续则退出此选项
        ans = input('是否继续修改其他学员的信息？ y/n')
        if ans == 'y':
            # 函数自己调用自己实现循环，不同于上面的 delete 方法，是两种方式
            modify()


def sort():
    show()
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as rf:
            stu_lst = rf.readlines()
        stu_new = []
        for i in stu_lst:
            d = dict(eval(i))
            stu_new.append(d)
    else:
        return
    asc_or_desc_bool = input('请选择（0.升序，1.降序）')
    if asc_or_desc_bool == '0':
        asc_or_desc_bool = False
    elif asc_or_desc_bool == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input(
        '请选择排序方式（1.按英语成绩排序  2.按 python 成绩排序  3.按 java 成绩排序  0.按总成绩排序）')
    if mode == '1':
        stu_new.sort(key=lambda i: int(i['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        stu_new.sort(key=lambda i: int(i['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        stu_new.sort(key=lambda i: int(i['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        stu_new.sort(key=lambda i: int(
            i['english'])+int(i['python'])+int(i['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_stu(stu_new)


def total():
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as rf:
            stu = rf.readlines()
            if stu:
                print(f'一共有 {len(stu)} 名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息！！！')


def show():
    stu_lst = []
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as rf:
            stu = rf.readlines()
            for i in stu:
                stu_lst.append(eval(i))
            if stu_lst:
                show_stu(stu_lst)
    else:
        print('暂未保存数据信息！！！')


if __name__ == '__main__':
    main()
