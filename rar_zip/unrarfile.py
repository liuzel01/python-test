#!/Users/aaron/py38env/bin/python3
# -*- coding: utf-8 -*-

import os
os.environ.setdefault("UNRAR_LIB_PATH","/Users/aaron/Downloads/unsplash/unrar/libunrar.so")
import sys
from somedecorators import timeit
from unrar import rarfile

@timeit()
def decompress(rar_file):
    rf = rarfile.RarFile(rar_file, mode='r') # mode的值只能为'r'
    rf_list = rf.namelist() # 得到压缩包里所有的文件
    for file in rf_list:
        print(file)
    rf.extractall()

if __name__ == '__main__':
    decompress(sys.argv[1])



