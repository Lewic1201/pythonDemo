from collections import deque
from copy import deepcopy


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = None

    # def array2tree(self, arr):
    #     leng = len(arr)
    #     index = 1
    #     self.root = Node(arr[0]) if arr else None
    #     queue = deque([self.root])
    #     while index < leng:
    #         node_child = queue.popleft()
    #         if node_child:
    #             node_child.left = Node(arr[index]) if arr[index] else None
    #             queue.append(node_child.left)
    #             index += 1
    #             if index >= leng:
    #                 break
    #             node_child.right = Node(arr[index]) if arr[index] else None
    #             queue.append(node_child.right)
    #             index += 1
    #     return self.root

    def array2tree(self, arr=None):
        if not arr:
            return
        self.root = Node(arr[0])
        leng = len(arr)
        index = 1
        queue = [self.root]
        while index < leng:
            tmp = queue[0]
            del queue[0]
            node_child = tmp
            if node_child:
                node_child.left = Node(arr[index]) if arr[index] else None
                queue.append(node_child.left)
                index += 1
                if index >= leng:
                    break
                node_child.right = Node(arr[index]) if arr[index] else None
                queue.append(node_child.right)
                index += 1
        return self.root

    def cengxu(self):
        queue = [self.root]
        ret = []
        while queue:
            node = queue[0]
            del queue[0]
            if node:
                ret.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def cengxu2(self):
        queue = [self.root]
        tmp = []
        ret = []
        deep = 0
        while queue:
            ret.append([])
            for i in queue:
                if not i:
                    continue
                ret[deep].append(i.value)
                tmp.append(i.left)
                tmp.append(i.right)
            queue = tmp
            deep += 1
            tmp = []
        ret.remove([])
        return ret

    def max_deep(self):
        queue = [self.root]
        tmp = []
        deep = 0
        while queue:
            for i in queue:
                if not i:
                    continue
                tmp.append(i.left)
                tmp.append(i.right)
            queue = tmp
            deep += 1
            tmp = []
        return deep-1

    def xianxu(self):
        ret = []

        def bianli(group):
            if not group:
                return
            ret.append(group.value)
            bianli(group.left)
            bianli(group.right)

        bianli(self.root)
        return ret

    def zhongxu(self):
        ret = []

        def bianli(group):
            if not group:
                return
            bianli(group.left)
            ret.append(group.value)
            bianli(group.right)

        bianli(self.root)
        return ret

    def houxu(self):
        ret = []

        def bianli(group):
            if not group:
                return
            bianli(group.left)
            bianli(group.right)
            ret.append(group.value)

        bianli(self.root)
        return ret


if __name__ == '__main__':
    pass
    a = Tree()
    # a.array2tree([1, 2, None, 3, None, 5, 3, None, 5])
    a.array2tree([1, 2, 3, 4, 5, 6, 7, 8])
    # a.array2tree([1, 2, 3, None, None, 6, 7, 8, None, 9, 10, 11, 12, None, 13])
    #
    # print(a.cengxu())
    # print(a.xianxu())
    # print(a.zhongxu())
    # print(a.houxu())
    print(a.cengxu())
    print(a.cengxu2())
    print(a.max_deep())

    # tr = Tree()
    # tr.root = Node(1)
