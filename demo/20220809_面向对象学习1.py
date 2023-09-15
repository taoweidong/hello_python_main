import uuid
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self):
        print("person init")
        self.sex = '未知'

    @abstractmethod
    def say(self):
        print("Person say hello")


class ZhangSan(Person):
    def say(self):
        pass

    def __init__(self):
        super(ZhangSan, self).__init__()


class TangTang(Person):
    def say(self):
        pass

    def __init__(self):
        super(TangTang, self).__init__()


class Student(Person):
    def say(self):
        # super(Student, self).say()
        pass

    def __init__(self, sid: str, name: str, age: int):
        super(Student, self).__init__()
        # 私有类型
        self.__sid = sid
        self.name = name
        # 保护属性
        self._age = age

    # def say(self):
    #     print("Student say hello")


class LiSi(ZhangSan, TangTang):
    def __init__(self):
        super().__init__()
        # super(LiSi, self).__init__()


if __name__ == '__main__':
    # # p = Person()
    # stu = Student(str(uuid.uuid4()), '张三', 10)
    # # print(stu.__dict__)
    # #
    # # print(stu.name)
    # # print(stu._age)
    # # print(stu.sex)
    #
    # print("*" * 10)
    # stu.say()

    l = LiSi()
