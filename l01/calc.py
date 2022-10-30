# 如何导入自定义模块（自己的）
from threading import main_thread
from pip import main


def add(a,b):
    return a + b
def div(a,b):
    return a / b

# 以主程序方式运行
if __name__ == '__main__':
    print(add(10,20))  # 只有当点击运行 cal 时，才会执行运算

