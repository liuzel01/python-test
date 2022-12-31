import platform
from pprint import pprint

__author__ = "liuzel01"
__EMAIL__ = "@hilonggroup.com"
# system = platform.system()
# uname = platform.uname()
# pprint(uname)

def check_feature(feature,string):
    if feature in string.lower():
        return True
    else:
        return False
def get_value_from_string(key,string):
    value = "NONE"
    for line in string.split("\n"):
        if key in line:
            value = line.split(":")[1].strip()
    return value

cpu_features = []

with open('/proc/cpuinfo') as cpus:
    cpu_data = cpus.read()
    num_of_cpus = cpu_data.count("processor")
    cpu_features.append("CPU 核心数: {0}".format(num_of_cpus))
    one_processor_data = cpu_data.split("processor")[1]
    # print (one_processor_data)
    if check_feature("vmx", one_processor_data):
        cpu_features.append("CPU Virtualization: enabled")
    if check_feature("cpu_meltdown", one_processor_data):
        cpu_features.append("已知错误: CPU Metldown ")
    model_name = get_value_from_string("CPU 型号名称 ", one_processor_data)
    cpu_features.append("CPU 型号名称: {0}".format(model_name))
    cpu_mhz = get_value_from_string("cpu MHz", one_processor_data)
    cpu_features.append("CPU 频率（Mhz）: {0}".format((cpu_mhz)))

memory_features = []
with open('/proc/meminfo') as memory:
    memory_data = memory.read()
    total_memory = get_value_from_string("MemTotal", memory_data).replace("kB", "")
    free_memory = get_value_from_string("MemFree", memory_data).replace("kB", "")
    swap_memory = get_value_from_string("SwapTotal", memory_data).replace("kB", "")
    total_memory_in_gb = "总内存（GB）: {0}".format(int(total_memory) / 1024)
    free_memory_in_gb = "空闲内存（GB）: {0}".format(int(free_memory) / 1024)
    swap_memory_in_gb = "SWAP内存（GB）: {0}".format(int(swap_memory) / 1024)
    memory_features = [total_memory_in_gb, free_memory_in_gb, swap_memory_in_gb]

print("============这是操作系统相关信息============")

print(""" 
服务器类型: {0}
主机名称: {1}
内核版本: {2}
操作系统版本: {3}
操作系统架构: {4}
Python 版本: {5}
""".format(platform.system(),
           platform.uname()[1],
           platform.uname()[2],
           platform.version(),
           platform.machine(),
           platform.python_version()
           ))

print("============这是CPU相关信息============")
print("\n".join(cpu_features))

print("\n============这是内存相关信息============")
print("\n".join(memory_features))
