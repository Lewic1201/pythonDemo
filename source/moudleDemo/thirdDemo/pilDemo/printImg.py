import matplotlib.pyplot as plt  # 约定俗成的写法plt
import matplotlib as mpl
import numpy as np


import seaborn as sns


def imgA():
    # 首先定义两个函数（正弦&余弦）
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # -π to+π的256个值
    C, S = np.cos(X), np.sin(X)
    plt.plot(X, C)
    plt.plot(X, S)
    # 在ipython的交互环境中需要这句话才能显示出来
    plt.show()


def imgB():
    sns.set()

    # 通过加载sns自带数据库中的数据（具体数据可以不关心）
    flights_long = sns.load_dataset("flights")
    flights = flights_long.pivot("month", "year", "passengers")

    # 使用每个单元格中的数据值绘制一个热力图heatmap
    sns.heatmap(flights, annot=True, fmt="d", linewidths=.5)
    plt.show()


def imgC():
    np.random.seed(sum(map(ord, "aesthetics")))

    # 首先定义一个函数用来画正弦函数，可帮助了解可以控制的不同风格参数
    def sinplot(flip=1):
        x = np.linspace(0, 14, 100)
        for i in range(1, 7):
            plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)

    sinplot()
    plt.show()

imgA()
imgB()
imgC()
