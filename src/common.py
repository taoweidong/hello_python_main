# -*- coding: utf-8 -*-
import datetime
import os
import shutil
import uuid


class CommonFun(object):
    @classmethod
    def get_current_date(cls):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date

    @classmethod
    def get_unique_id(cls):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")  # 获取当前时间戳并格式化
        unique_id = f"{timestamp}{str(uuid.uuid4().hex)}"  # 使用时间戳和 uuid 生成唯一 ID
        return unique_id

    @classmethod
    def clear_path(cls, path):
        try:
            if not os.path.exists(path):  # 判断路径是否存在
                os.makedirs(path)  # 递归创建路径
            else:
                shutil.rmtree(path)  # 清理目录
                os.makedirs(path)  # 创建路径
        except Exception as e:
            print("创建或清理目录出现异常:", str(e))
