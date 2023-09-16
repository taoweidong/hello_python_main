# -*- coding: utf-8 -*-
import datetime
import unittest

from src.common import CommonFun


class TestCommonFun(unittest.TestCase):
    def test_get_current_date(self):
        # 调用待测试的方法
        result = CommonFun.get_current_date()

        # 检查结果的类型和格式
        self.assertIsInstance(result, str)
        self.assertRegex(result, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

        # 检查结果是否为当前日期
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_date)
        self.assertEqual(result, current_date)

    def test_generate_unique_id(self):
        result = CommonFun.get_unique_id()
        print(result)
