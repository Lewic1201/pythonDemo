from random import randint

"""
二维数组按指定列优先级的顺序排序
(优先级高的列先排序,然后此列值相同的再按下一个优先级的列排序,以此类推)
"""


def create_double_array():
    data = []
    for i in range(50):
        row = []
        for i in range(20):
            num = randint(0, 4)
            row.append(num)
        data.append(row)
    print(data)
    return data


def sorts(data, column_level=None):
    """
    二维数组按指定列优先级的顺序排序
    :param data: 二维数组
    :param column_level: 列的优先级,[列下标,...]
    :return:
    """
    if column_level is None:
        column_level = [i for i in range(len(data[0]))]
    for i in range(len(data) - 1):
        m = 0
        j = i + 1
        while j in range(i + 1, len(data)):
            k = column_level[m]
            if data[i][k] > data[j][k]:
                data[i], data[j] = data[j], data[i]
            elif data[i][k] == data[j][k]:
                if m < len(column_level):
                    m += 1
                    continue
            m = 0
            j += 1
    return data


if __name__ == '__main__':
    data = create_double_array()
    # data = [[2, 0, 3, 4, 4], [4, 3, 4, 1, 4], [2, 2, 2, 3, 3], [0, 0, 4, 4, 2], [2, 3, 1, 3, 0]]
    new_data = sorts(data)

    print(new_data)
