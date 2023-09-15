import threading

import pymysql as pymysql


class Schedular(object):
    def __init__(self):
        self._lock = threading.RLock()
        self.start = 0
        # 每次取10000条数据
        self.step = 10000

    def get_data(self):
        # 上锁,避免多线程同时对数据库进行访问，取出重复数据
        self._lock.acquire()
        # 查询数据库，进行取数操作

        mydb = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               database='test')
        cursor = mydb.cursor()  # 和前面一样，下面为了简洁统统省略
        sql = "SELECT * FROM tb_user LIMIT {},{}".format(self.start, self.start + self.step)
        print(sql)
        cursor.execute(sql)  # 执行sql语句，结果赋给mycursor
        data = cursor.fetchall()  # 用了 fetchall() 方法，该方法从最后执行的语句中获取所有行，结果赋给myresult。
        # for x in data:
        #     print(x)  # 遍历myresult结果（下面为了简洁统统省略）
        print(len(data))
        # 取数完成，指针移动
        self.start += self.step
        # 解锁
        self._lock.release()

        return data


def process_data():
    # 从实例中提取数据
    # 从该实例中提取数据
    data = scheduler.get_data()
    while data:
        # 进行处理数据的具体操作:
        # 去重、补缺、运算...只要还有数据，本线程就继续取新数据
        # 然后再获取数据，进行循环
        data = scheduler.get_data()


# 创建多线程
def threads_scheduler(thread_num):
    threads = []
    for i in range(thread_num):
        # 创建线程
        td = threading.Thread(target=process_data, name='th_' + str(i))
        threads.append(td)

    for t in threads:
        # 启动线程
        t.start()
        for t in threads:
            # 子线程守护
            t.join()
            print("数据已全部处理完成")


if __name__ == '__main__':
    # 实例化一个调度器，初始化参数
    scheduler = Schedular()
    # 创建线程，开始处理数据
    threads_scheduler(3)
