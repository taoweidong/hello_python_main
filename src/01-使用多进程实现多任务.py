import logging

# 第一步：导入进程包
import multiprocessing
import os
from time import sleep


def write(num):
    for i in range(num):
        print(f"我是任务1，开始启动执行了。。。。。{i}-----{os.getpid()}-----{os.getppid()}")
        sleep(2)


def say(num):
    for i in range(num):
        print(f"我是任务2，开始启动执行了。。。。。{i}-----{os.getpid()}-----{os.getppid()}")
        sleep(2)


if __name__ == '__main__':
    # thread = multiprocessing.Process(target=write, name='thread1111', args=(4,))
    # thread1 = multiprocessing.Process(target=say, name='thread2222', kwargs={"num": 5})
    # thread.start()
    # thread1.start()

    print("*" * 20)

    pool = multiprocessing.Pool(processes=10)
    for i in range(6):
        pool.apply_async(func=say, args=(3,))
    pool.close()
    pool.join()
