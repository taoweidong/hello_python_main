# -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import TimedRotatingFileHandler


class FileSearchLogger:
    @staticmethod
    def setup_logging():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 创建并配置控制台处理程序
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 获取当前文件所在的目录路径
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')

        # 检查目录是否存在，如果不存在则创建
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建并配置文件处理程序，使用TimedRotatingFileHandler实现按时间分割文件
        log_file = os.path.join(log_dir, 'log_file.log')
        # when='D'表示每天分割一次日志，interval=1表示间隔为1天，backupCount=7表示最多保留7个备份文件。
        file_handler = TimedRotatingFileHandler(log_file, when='D', interval=1, backupCount=7)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
