#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 【Python】Python多进程详解：https://zhuanlan.zhihu.com/p/493699150

import os
import random
import time
from multiprocessing import Process, Queue


def recv(q):
    print(f'子进程：接收进程（{os.getpid()}）开始！')
    while True:
        # 用产生随机数的方法模拟数据的接收
        data = random.randint(1, 100)
        print(f'子进程：接收进程接收到数据{data}！')
        q.put(data)
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)


def send(q):
    print(f'子进程：转发进程（{os.getpid()}）开始！')
    while True:
        # 注意：如果q里面没有数据，get()方法就会等待，直到获得一个数据并赋值给data
        data = q.get()
        print(f'子进程：转发进程接收到数据{data}并开始处理、转发！')
        time.sleep(1)


if __name__ == '__main__':
    print(f'主进程（{os.getpid()}）开始...')
    q = Queue()
    p1 = Process(target=recv, args=(q,))
    p2 = Process(target=send, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
