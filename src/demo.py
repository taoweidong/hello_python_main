# -*- coding: utf-8 -*-
from collections import Counter

from loguru import logger


def sql(x):
    return x * 5


def chunk(list_data, size):
    """
    把指定数组按照size大小分割
    Args:
        list_data:
        size:

    Returns:

    """
    return [list_data[i:i + size] for i in range(0, len(list_data), size)]


if __name__ == '__main__':
    logger.info("test.......")
    temp_list = [1, 2, 3, 4, 5, 6, 7]
    temp_list2 = ['a', 'b', 'c', 'd', 'e', 'f']
    logger.info("*" * 50)
    logger.info(list(zip(temp_list, temp_list2)))
    logger.info("*" * 50)
    # 列表推导式
    temp = [i * 2 for i in temp_list]
    logger.info(temp)

    fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
    temp_dict = Counter(fruits)
    for k, v in temp_dict.items():
        logger.info(k, v)
    logger.info(type(Counter(fruits)))
    logger.info(Counter(fruits))

    # map函数使用方法
    mm = map(sql, temp_list)
    logger.info([i for i in mm])
    logger.info("*" * 50)
    for i in chunk(temp_list, 3):
        logger.info(i)
