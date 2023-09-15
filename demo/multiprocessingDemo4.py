#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 功能：https://www.jb51.net/article/173328.htm
import multiprocessing
import os
import random
import time


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
    # 创建进程池
    pool = multiprocessing.Pool(4)
    # 创建进程池队列
    queue = multiprocessing.Manager().Queue()
    # 在进程池中的进程间进行通信
    # 使用线程池同步的方式，先写后读
    # pool.apply(write_data, (queue, ))
    # pool.apply(read_data, (queue, ))
    # apply_async() 返回ApplyResult 对象
    result = pool.apply_async(recv, (queue,))
    # ApplyResult对象的wait() 方法，表示后续进程必须等待当前进程执行完再继续
    # result.wait()
    pool.apply_async(send, (queue,))
    pool.close()
    # 异步后，主线程不再等待子进程执行结束，再结束
    # join() 后，表示主线程会等待子进程执行结束后，再结束
    pool.join()
