#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 17:32
# @Author  : li_panfeng
# @File    : lc_bin_tree.py
# @Software: PyCharm
# @context :

from source.utils.decorators import print_cls


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        左叶子之和
        :param root:
        :return:
        """
        pass



if __name__ == '__main__':
    ss = Solution()
