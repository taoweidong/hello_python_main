#!/usr/bin/env python
# 单元测试：https://liaoxuefeng.com/books/python/error-debug-test/unit-test/
import sys
import unittest

from loguru import logger

# logger.add(
#     sys.stdout,
#     level="INFO",
#     format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
# )


class TesthelloPythonMain(unittest.TestCase):
    """
    单元测试：https://liaoxuefeng.com/books/python/error-debug-test/unit-test/
    """

    def setUp(self):
        """每调用一个测试方法的前执行"""
        logger.info("测试开始")

    def tearDown(self):
        """每调用一个测试方法的后执行"""
        logger.info("测试结束")

    def test_000_something(self):
        a = 20 + 3
        self.assertEqual(a, 23, "测试沒有通过")

    def test_002_something(self):
        a = 20 + 222
        self.assertEqual(a, 23, "测试沒有通过")
