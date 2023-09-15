import collections

# 模块全局变量
_global = object()
# 全局可见的全局变量
overall_global = object()

# 全局常量
CONSTANT = 60 * 60


def wrong_example():
    for i in range(100):
        if i == 10:
            # raise StopIteration()  不推荐的方式，退出迭代
            return  # 正确实例
        yield i


for i in wrong_example():
    print(i)

if __name__ == '__main__':
    student = collections.namedtuple("Student", ["name", "age"])

    print(student)
    print(type(student))

    print(_global)
    print(overall_global)
    print(CONSTANT)
