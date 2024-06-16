# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class Animal(Enum):
    ANT = 1
    BEF = 2


print(Animal)


class Employee:
    # 类属性
    class_version = "1.0"

    # 类的私有属性
    __class_v = "11111"

    def __init__(self, name):
        self.name = name

    def __test(self):
        print(self.name)

    @classmethod
    def cls_ver_get(cls):
        return cls.__class_v

    @classmethod
    def cls_ver_set(cls):
        cls.__class_v = cls.__class_v + "===R"

    @staticmethod
    def static_get():
        print("KK" * 10)


if __name__ == '__main__':
    Employee.static_get()
    print("*" * 30)
    emp = Employee("张三")
    print(emp)
    for i in dir(emp):
        print(i)
    print("*" * 30)
    # 打印继承关系
    print(Employee.__mro__)
    # print(Employee.__test())
    print(Employee.class_version)
    print(emp.class_version)
    emp.class_version = "2.0"
    print(emp.class_version)
    # 类的私有属性不能访问
    # print(emp.__class_v)
    print("*" * 20)
    print(emp.cls_ver_get())
    emp.cls_ver_set()
    print(emp.cls_ver_get())

    print("*" * 50)
    print(isinstance(object, type))
    print(isinstance(type, object))
    print(isinstance(type, type))
    print(isinstance(object, object))

    a = 1
    print(id(a), type(a), a)
    print(id(a))
    print(id(a))

    print(id(int), type(int), int)
    print(id(type), type(type), type)

    print(int.__bases__)
    print(type.__bases__)
