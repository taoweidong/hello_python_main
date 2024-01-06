# -*- coding: utf-8 -*-
# 学习链接：https://mp.weixin.qq.com/s/3RHRathfd-xapBlVgFfL7w

import numpy as np

# 创建一维数组
arr1 = np.array([1, 2, 3])
print(arr1)

# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 创建全零数组
zeros_arr = np.zeros((3, 3))
print(zeros_arr)

# 创建全一数组
ones_arr = np.ones((2, 2))
print(ones_arr)

# 创建等差数组
range_arr = np.arange(0, 10, 2)
print(range_arr)

# 创建均匀分布数组
uniform_arr = np.linspace(0, 1, 5)
print(uniform_arr)

# 创建随机数组
rand_arr = np.random.rand(2, 2)
print(rand_arr)
