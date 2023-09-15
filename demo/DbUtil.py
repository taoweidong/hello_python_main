#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sre_constants import CHARSET

import pymysql

config = {
    'host': '127.0.0.1',
    'db': 'test',
    'user': 'root',
    'port': 3306,
    'password': 'root'
}

dbg_config = {
    'host': '127.0.0.1',
    'db': 'test',
    'user': 'root',
    'port': 3306,
    'password': 'root'
}


class DbUtil(object):
    """
    MySql操作类，对mysql数据库进行增删改查
    """

    def __init__(self, config):

        try:
            self.connection = pymysql.Connect(**config)
            self.connection.autocommit(True)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            return False

    def re_connect(self):
        try:
            self.connection.ping()
        except:
            self.connection()

    def query_all(self, sql):
        # 如果与数据库断开即重连
        self.re_connect()
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__ == '__main__':
    db_util = DbUtil(dbg_config)
    db_util.re_connect()

    result = db_util.query_all('select * from tb_user')
    print(len(result))
