# -*- coding: utf-8 -*-
# 链接：https://mp.weixin.qq.com/s/-tD3IWSE9m9-Gzna7kiEHA
import numpy as np
from PIL import Image

# 读取图像
image_path = r"E:\婚礼\婚纱照-精修OK\AI0I0337-大框.jpg"
image = Image.open(image_path)
print(image.size, image.format, image.mode)
# display(image)

# 转换为NumPy数组
image_array = np.array(image)

# 图像缩放
size = (image.size[0] // 2, image.size[1] // 2)

resize = Image.fromarray(image_array, 'RGB').resize(size)

# 显示原图和缩放后的图
display(image, resize)
resized_image = np.array(resize)

# 提取颜色通道
red_channel = resized_image[:, :, 0]
green_channel = resized_image[:, :, 1]
blue_channel = resized_image[:, :, 2]
print(red_channel, green_channel, blue_channel)
