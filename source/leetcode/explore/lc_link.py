#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 20:37
# @Author  : Administrator
# @File    : lc_main.py
# @Software: PyCharm
# @context :
def prints(func):
    def wrapper(self, *args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]: ", *args)
            ret = func(self, *args, **kwargs)
            print("[RESULT]: ", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s->%s' % (self.val, self.next)


class Solution:

    @prints
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)

        def add_ls(ls1, ls2, ret):
            ls12 = 0
            if ls1 is None and ls2 is None:
                if not ret.val:
                    return None
                else:
                    return ListNode(1)
            elif ls1 is None:
                ls1 = ListNode(0)
            elif ls2 is None:
                ls2 = ListNode(0)
            ret.val += (ls1.val + ls2.val)
            if ret.val < 10:
                ret.next = add_ls(ls1.next, ls2.next, ListNode(0))
                return ret
            else:
                ret.val -= 10
                ret.next = add_ls(ls1.next, ls2.next, ListNode(1))
                return ret

        return add_ls(l1, l2, ret)

    @prints
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = None
        while head:
            tmp = ret
            ret = ListNode(head.val)
            ret.next = tmp
            head = head.next
        return ret


if __name__ == '__main__':
    ss = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    # l1 = ListNode(5)
    # l2 = ListNode(5)
    # l1 = ListNode(1)
    # l2 = ListNode(9)
    # l2.next = ListNode(9)
    # a = ss.addTwoNumbers(l1, l2)
    # prints(123)
    ss.reverseList(l1)
