# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2022/9/28 22:32
# @Author    :Taoweidong
# -*- coding:utf-8 -*-
import math

import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


def get_single_data_frame(cur_path):
    print(f"读取文件{cur_path}")
    return cur_path


def get_file_list(root_path):
    file_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # print(file)     #文件名
            print(os.path.join(root, file))
            file_list.append(os.path.join(root, file))
    return file_list


def split_list(input_list, per_list_len):
    """
    把输入的input_list列表，分成per_list_len份
    :param input_list:输入列表
    :param per_list_len:拆分的份数
    :return:拆分之后的列表
    """
    result_list = []
    if len(input_list) <= per_list_len or per_list_len < 1:
        # 如果列表中的数据小于份数，则不需要进行分组了，直接返回
        result_list.append(input_list)
        return result_list
    # 分成10份
    h = 0
    for i in range(0, per_list_len):
        m = math.ceil(len(input_list) / per_list_len)
        if i == per_list_len - 1:
            obj = input_list[h:]
        else:
            obj = input_list[h:h + m]
        if len(obj) != 0:
            result_list.append(obj)
        h = h + m
    return result_list


# 创建两个线程
def get_sample(file_dir):
    executor = ThreadPoolExecutor(max_workers=10)
    all_file_list = os.listdir(file_dir)
    data_frame_list = []
    all_task = []
    for single_file in all_file_list:
        cur_path = os.path.join(file_dir, single_file)
        if "_SUCCESS" in cur_path or "_COPYING_" in cur_path:
            continue
        try:
            task = executor.submit(get_single_data_frame, cur_path)
            # single_data_frame = executor.submit(get_single_data_frame, cur_path).result()
            # data_frame_list.append(single_data_frame)
            all_task.append(task)
        except:
            print("Error: 读取异常")
    wait(all_task)
    for future in as_completed(all_task):
        result = future.result()
        data_frame_list.append(result)
    # all_data_frame = pd.concat(data_frame_list, ignore_index=True)
    return data_frame_list


root_path = r"D:\workspace\kernel_liteos_a"

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(len(data_list))
print(split_list(data_list, 0))

# print(get_file_list(root_path))

# print(get_sample(root_path))
