# -*- coding: utf-8 -*-
for x in range(1, 10):  # x是乘数
    for y in range(1, x + 1):  # 主是被乘数
        result = f"{x * y}".rjust(2)
        print(f"{y}x{x}={result}".ljust(8), end = '')  # 使用新特性格式化字符串，也可以使用format,%等格式化，其中ljust（6）左对齐，长度为6，右补空格
    print("")  # 打印一个换行
