# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right
#
#     def set_left(self, value):
#         self.left = value
#
#     def set_right(self, value):
#         self.right = value


'''
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
[1,null,2,null,3]
   1
    \
     2
      \
       3 

'''


def array2tree(arr):
    arr = [1, None, 2, 3]
    ret = None
    for k, v in enumerate(arr):
        if v:
            ret = TreeNode(v)
        pass


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用列表构建二叉树，以及二叉树的层次遍历，先序遍历，中序遍历，后序遍历的代码如下所示：

from collections import deque


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    
    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)

        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret


# test
t = Tree()
t.construct_tree([1, 2, None, 4, 3, None, 5])
print(t.bfs())
# print(t.pre_traversal())
# print(t.in_traversal())
# print(t.post_traversal())
