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

fname = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input'请选择： ')
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                ans = input('????????????? y/n')
                if ans == 'y' or ans == 'Y':
                    print('�ݧ�?????????????????????')
                    # ?????
                    break
                else:
                    continue
            elif choice == 1:
                # ?????????
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
        id = input('???????????? ID???? 1001?? ?? ')
        if not id:
            break
        name = input('??????????????? ').strip()
        if not name:
            break
        try:
            english = int(input('?????? ??? ????? ').strip())
            python = int(input('?????? python ????? ').strip())
            java = int(input('?????? java ????? ').strip())
        except:
            print('??????��?????????????????????????')
            continue
        # ???????????????��???
        stu_info = {'id': id, 'name': name,
                    'english': english, 'python': python, 'java': java}
        # ??????????????��???
        stu_lst.append(stu_info)
        ans = input('??????????? y/n')
        if ans == 'y':
            continue
        else:
            break
    # ???? save() ????
    save(stu_lst)
    print('?????????????????')


def save(stu_lst):
    try:
        stu_txt = open(fname, 'a', encoding='utf-8')
    except:
        stu_txt = open(fname, 'w', encoding='utf-8')
    for i in stu_lst:
        stu_txt.write(str(i)+'\n')
    stu_txt.close()


def search():
    pass


def delete():
    while 1:
        stu_id = input('???????????????ID?? ').strip()
        if stu_id != '':
            if os.path.exists(fname):
                with open(fname, 'r', encoding='utf-8') as f:
                    stu_old = f.readlines()
            else:
                stu_old = []
            # ?????????
            flag = False
            if stu_old:
                with open(fname, 'w', encoding='utf-8') as fw:
                    d = {}
                    for i in stu_old:
                        # ???????????????
                        d = dict(eval(i))
                        if d['id'] != stu_id:
                            fw.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id ?{stu_id}??????????????')
                    else:
                        print(f'??????id ?{stu_id}????????')
            else:
                print('????????')
                break
            # ???????????????????????
            show()
            ans = input('??????????? y/n')
            if ans == 'y':
                continue
            else:
                break


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()
