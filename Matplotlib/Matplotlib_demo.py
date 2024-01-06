# -*- coding: utf-8 -*-
# 学习链接：https://mp.weixin.qq.com/s/3RHRathfd-xapBlVgFfL7w
import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 23, 8, 10]
# 绘制折线图
plt.plot(x, y)
# 添加标题和标签
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
# 显示图形
plt.show()
