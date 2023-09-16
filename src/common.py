# -*- coding: utf-8 -*-
import datetime
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
        unique_id = f"{timestamp}_{str(uuid.uuid4().hex)}"  # 使用时间戳和 uuid 生成唯一 ID
        return unique_id
