#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 功能：多线程的方式将srcDir目录下文件拷贝到dstDir目录下
import os
import shutil
import time
from multiprocessing import Pool

srcDir = r"D:\workspace\test"
dstDir = r"D:\workspace\distcc-master-test"


# 拷贝文件的函数
def copy_file(file):
    file_path = os.path.join(srcDir, file)
    dst_file_path = os.path.join(dstDir, file)
    time.sleep(0.02)
    shutil.copy(file_path, dst_file_path)


if __name__ == '__main__':
    shutil.rmtree(dstDir) if os.path.exists(dstDir) else True
    files = os.listdir(srcDir)
    # 创建目标路径
    os.makedirs(dstDir) if not os.path.exists(dstDir) else False

    # 多线程处理
    pool = Pool(16)
    t_start = time.time()
    # 第一个参数是一个函数，第二个参数是一个列表，函数中逐个处理列表中的每一个元素
    pool.map(copy_file, files)
    t_end = time.time()
    print(f"time is :{t_end - t_start}")
    pool.close()
    pool.join()
