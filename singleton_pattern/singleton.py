# -*- coding: utf-8 -*-
import threading


class Singleton:
    _instances = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instances is None:
                cls._instances = super().__new__(cls)
        return cls._instances

    def __init__(self, value):
        # 防止在多线程环境下重复初始化
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True


if __name__ == '__main__':
    def t_singleton(value):
        singleton = Singleton(value)
        print(f"创建对象，单例对象的值: {singleton.value}")
        return singleton


    threads = [
        threading.Thread(target=t_singleton, args=(1,)),
        threading.Thread(target=t_singleton, args=(233,))
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    singleton1 = Singleton(1)
    singleton2 = Singleton(2333)

    print(singleton1.value)
    print(singleton2.value)

    print(singleton1 is singleton2)
