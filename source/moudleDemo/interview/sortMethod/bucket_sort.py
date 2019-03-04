import random


class bucketSort(object):
    """
    桶排序:
    取数组最大值和最小值,构建一个长度为max_value-min_value+1的桶,[0,0,0,...]
    获取每个位置的数的个数,重新构建结果

    适合:只能是整数,最大最小值间距越小,速度越快

    """

    def _max(self, oldlist):
        _max = oldlist[0]
        for i in oldlist:
            if i > _max:
                _max = i
        return _max

    def _min(self, oldlist):
        _min = oldlist[0]
        for i in oldlist:
            if i < _min:
                _min = i
        return _min

    def sort(self, oldlist):
        # 获取边界值
        _max = self._max(oldlist)
        _min = self._min(oldlist)

        # 构建桶
        s = [0 for i in range(_min, _max + 1)]
        for i in oldlist:
            s[i - _min] += 1
        current = _min

        # 构建结果
        n = 0
        for i in s:
            while i > 0:
                oldlist[n] = current
                i -= 1
                n += 1
            current += 1
        return oldlist


if __name__ == '__main__':
    a = [random.randint(0, 100) for i in range(10)]
    print('origin:', a)
    bucketSort().sort(a)
    print('result:', a)
