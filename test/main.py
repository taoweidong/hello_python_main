# -*- coding: utf-8 -*-
import unittest

from BeautifulReport import BeautifulReport

# 创建一个测试套件


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    # 测试结果输出在Html
    test_dir = "./"
    # 然后创建集合对象
    dis = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    runner = BeautifulReport(dis)
    runner.report(
        description="描述信息",
        filename="BeautifulReport"  # 生成测试报告的文件名
    )
