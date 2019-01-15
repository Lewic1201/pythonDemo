''' 二叉树的建立及实现 (递归与非递归) '''
from collections import deque


# 树节点的定义
class Node:
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.lchild = lchild  # 表示左子树
        self.rchild = rchild  # 表示右子树
        self.data = data  # 表示数据域


class Create_Tree:
    def __init__(self):
        self.root = Node()  # 表示结点
        self.myQueue = deque()  # 使用队列不会有太多的内存开销

    # 按层次生成树
    def add(self, elem):
        node = Node(elem)
        # 根节点
        if self.root.data == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 记录结点
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.popleft()  # 弹出已经处理好左右子树的父结点

    # 递归建树
    def traversal_create(self, root):
        data = input()
        if data is None:
            return None
        else:
            root.data = data
            root.lchild = self.traversal_create(root.lchild)
            root.rchild = self.traversal_create(root.rchild)
        return root

    # 前序遍历输出
    def digui(self, root):
        if root is None:
            return
        print(root.data)
        self.digui(root.lchild)
        self.digui(root.rchild)

    # 使用堆栈来遍历
    def stack_traversal(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while node or mystack:
            while node:
                print(node.data)
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            node = node.rchild

    # 层次遍历 使用队列
    def queue_tarversal(self, root):
        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            node = q.pop()
            print(node.data)
            if node.lchild is not None:
                q.append(node.lchild)
            else:
                q.append(node.rchild)
