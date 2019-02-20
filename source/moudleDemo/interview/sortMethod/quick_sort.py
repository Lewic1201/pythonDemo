import random


# quick sort
def quickSort(array):
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
        return quickSort(less) + equal + quickSort(greater)


if __name__ == '__main__':
    a = [random.randint(0, 100) for i in range(100)]
    print('origin:', a)
    ret = quickSort(a)
    print('result:', ret)