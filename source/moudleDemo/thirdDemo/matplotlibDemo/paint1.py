import math
import numpy as np  # 画图过程中会使用numpy
import pandas as pd  # 画图过程中会使用pandas

from pylab import *
from matplotlib import pyplot as plt  # 为方便简介为plt


def a_test():
    n = 256
    x = np.linspace(-np.pi, np.pi, n, endpoint=True)
    y = np.sin(2 * x)

    plot(x, y + 1, color='blue', alpha=1.00)
    plot(x, y - 1, color='blue', alpha=1.00)
    show()


def b_test():
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)

    scatter(x, y)
    show()


def base_test():
    x = np.linspace(-1, 1, 50)  # 定义x数据范围
    y1 = 2 * x + 1  # 定义y数据范围
    y2 = x ** 2
    y = y2
    plt.figure()  # 定义一个图像窗口
    plt.plot(x, y)  # plot()画出曲线
    plt.show()  # 显示图像


def tuoyuan():
    """椭圆"""
    x = np.linspace(-1, 1, 50)
    y1 = math.sqrt(1 - x ** 2)
    y2 = -math.sqrt(1 - x ** 2)
    plt.figure()
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()


def test_sin():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # 生成-π到+π的256个元素的等差数列
    c, s = np.cos(x), np.sin(x)  # 生成x的正弦余弦函数并赋值给c，s
    # plt.plot(x, c)  # 画出x与c的图像
    # plt.plot(x, s)  # 画出x与s的图像

    plt.figure(figsize=(10, 6), dpi=80)  # 设置图表的宽高比为10:6，设置dpi为80
    plt.plot(x, c, color="blue", linewidth=2.5, linestyle="-")  # 设置余弦函数颜色为蓝色，线宽2.5，样式为连线
    plt.plot(x, s, color="red", linewidth=2.5, linestyle="-")

    plt.show()  # 展示图像


# base_test()
# tuoyuan()
test_sin()
