import threading
import time
import random

from source.utils.decorators import times
from source.moudleDemo.interview.practise_interview.sortMillions.save import *


# num_list = queue_list()

@times
def quickSort0(nums):
    """原始快速排序"""

    def inner(array):
        if len(array) < 2:  # 基线条件（停止递归的条件）
            return array
        else:  # 递归条件
            baseValue = array[0]  # 选择基准值
            less, equal, greater = [], [baseValue], []
            for m in array[1:]:
                if m < baseValue:
                    # 由所有小于基准值的元素组成的子数组
                    less.append(m)
                elif m > baseValue:
                    # 由所有大于基准值的元素组成的子数组
                    greater.append(m)
                else:
                    # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
                    equal.append(m)
            return inner(less) + equal + inner(greater)

    return inner(nums)


def middle_axis(array):
    l, r = 0, len(array) - 1
    mid = (l + r) // 2
    if array[l] > array[mid]:
        array[l], array[mid] = array[mid], array[l]
    if array[r] < array[mid]:
        if array[r] < array[l]:
            array[l], array[mid], array[r] = array[r], array[l], array[mid]
        else:
            array[mid], array[r] = array[r], array[mid]
    print(array[l], array[mid], array[r])
    return array[mid]


def insertSort(array):
    for i in range(1, len(array)):  # 默认第一个元素已经在有序序列中，从后面元素开始插入
        for j in range(i, 0, -1):  # 逆向遍历比较，交换位置实现插入
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    print('after sort:', array)
    return array


@times
def quickSort1(nums):
    """优化选取中轴"""

    def middle_axis(array):
        left, right = 0, len(array) - 1
        mid = (left + right) // 2
        if array[left] >= array[mid]:
            if array[left] <= array[right]:
                return array[left]
            else:
                if array[mid] >= array[right]:
                    return array[mid]
                else:
                    return array[right]
        else:
            if array[left] <= array[right]:
                if array[mid] < array[right]:
                    return array[mid]
                else:
                    return array[right]
            else:
                return array[left]

    def inner(array):
        if len(array) < 2:  # 基线条件（停止递归的条件）
            return array
        else:  # 递归条件
            baseValue = middle_axis(array)  # 选择基准值
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
            return inner(less) + equal + inner(greater)

    return inner(nums)


@times
def quickSort2(nums):
    """优化选取中轴"""

    def middle_axis(array):
        l, r = 0, len(array) - 1
        mid = (l + r) // 2
        if array[l] > array[mid]:
            array[l], array[mid] = array[mid], array[l]
        if array[r] < array[mid]:
            if array[r] < array[l]:
                array[l], array[mid], array[r] = array[r], array[l], array[mid]
            else:
                array[mid], array[r] = array[r], array[mid]
        return array[mid]

    def inner(array):
        if len(array) < 2:  # 基线条件（停止递归的条件）
            return array
        else:  # 递归条件
            baseValue = middle_axis(array)  # 选择基准值
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
            return inner(less) + equal + inner(greater)

    return inner(nums)


@times
def quickSort3(nums):
    """长度短的使用插入排序"""

    def middle_axis(array):
        left, right = 0, len(array) - 1
        mid = (left + right) // 2
        if array[left] >= array[mid]:
            if array[left] <= array[right]:
                return array[left]
            else:
                if array[mid] >= array[right]:
                    return array[mid]
                else:
                    return array[right]
        else:
            if array[left] <= array[right]:
                if array[mid] < array[right]:
                    return array[mid]
                else:
                    return array[right]
            else:
                return array[left]

    def insert(array):
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
        # print('after sort:', array)
        return array

    def inner(array):
        if len(array) < 2:  # 基线条件（停止递归的条件）
            return array
        elif len(array) < 7:
            return insert(array)
        else:  # 递归条件
            baseValue = middle_axis(array)  # 选择基准值
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
            return inner(less) + equal + inner(greater)

    return inner(nums)


def save_ret(datas):
    with open('data_new_list.txt', 'w') as ff:
        for i in datas:
            ff.write(str(i))
            ff.write('\n')


if __name__ == '__main__':
    # num_list = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    num_list = [random.randint(0, 1000000) for i in range(300000)]
    # print(ret0)

    # print(num_list)
    ret = quickSort0(num_list)
    ret = quickSort1(num_list)
    ret = quickSort2(num_list)
    ret = quickSort3(num_list)

    # save_ret(ret)
    # print(ret)

    # print(middle_axis([122, 34, 75]))
    # for i in range(20):
    #     num_list = [random.randint(0, 100) for j in range(30)]
    #     # middle_axis(num_list)
    #     insertSort(num_list)
