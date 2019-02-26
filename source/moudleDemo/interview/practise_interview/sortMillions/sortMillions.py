import threading
import time

from source.moudleDemo.interview.practise_interview.sortMillions.save import *

num_list = queue_list()


def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        less, equal, greater = [], [baseValue], []
        flag = False
        for m in array:
            if flag:
                if m < baseValue:
                    # 由所有小于基准值的元素组成的子数组
                    less.append(m)
                elif m > baseValue:
                    # 由所有大于基准值的元素组成的子数组
                    greater.append(m)
                else:
                    # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
                    equal.append(m)
            else:
                flag = True
        return quickSort(less) + equal + quickSort(greater)


def save_ret(datas):
    with open('data_new_list.txt', 'w') as ff:
        for i in datas:
            ff.write(str(i))
            ff.write('\n')


if __name__ == '__main__':
    start = time.time()

    # array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    ret = quickSort(num_list)

    end = time.time()

    save_ret(ret)
    print(ret)
    print(end - start)
