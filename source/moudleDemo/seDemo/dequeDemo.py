from collections import deque

# 创建
a_list = [1, 2, 3, 4]
b_deque = deque([1, 2, 3, 4])

# 在列表末尾添加新的对象
a_list.append(5)
b_deque.append(5)

# 统计某个元素在列表中出现的次数
a_list.count(2)
b_deque.count(2)

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
a_list.extend([6, 7, 8])
b_deque.extend([6, 7, 8])

# 从列表中找出某个值第一个匹配项的索引位置
a_list.index(5)
b_deque.index(5)

# 将对象插入列表
a_list.insert(3, 111)
b_deque.insert(3, 111)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
a_list.pop()
b_deque.pop()

# 移除列表中某个值的第一个匹配项
a_list.remove(3)
b_deque.remove(3)

# 反向列表中元素
a_list.reverse()
b_deque.reverse()

# 清空列表
a_list.clear()
b_deque.clear()

# 复制列表
a_list.copy()
b_deque.copy()

b_deque = deque([4, 7, 1, 5, 8])

# 从左侧移除列表中的一个元素，并且返回该元素的值
b_deque.popleft()


# ---用list实现也不是不可，只不过有点麻烦~~~
def leftpop(lists):
    x = lists[0]
    del lists[0]
    return x


leftpop(a_list)

# 在列表首端一次性追加另一个序列中的多个值
b_deque.extendleft([1, 2])

# 限制deque的长度
c_deque = deque([1, 2, 3, 4], maxlen=4)
c_deque.append(5)  # 此时会在末尾加入5，同时删除最前面的1。
