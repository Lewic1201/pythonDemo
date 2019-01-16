#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 20:37
# @Author  : Administrator
# @File    : lc_main.py
# @Software: PyCharm
# @context :
def printdef(func):
    def wrapper(*args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]: ", *args)
            ret = func(*args, **kwargs)
            print("[RESULT]:", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper


def prints(func):
    def wrapper(self, *args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]:  ", *args)
            ret = func(self, *args, **kwargs)
            print("[RESULT]: ", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper


# @printdef
def list2link(nodes):
    ret = None
    for i in nodes[::-1]:
        tmp = ret
        ret = ListNode(i)
        ret.next = tmp
    return ret


# @printdef
def link2list(link):
    ret = []
    while True:
        if link:
            ret.append(link.val)
            link = link.next
        else:
            return ret


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

    @prints
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is None:
        #     return l2
        #
        # def getNext(link, link2):
        #     if link.next is None:
        #         link.next = link2
        #     else:
        #         return getNext(link.next, link2)
        #
        # getNext(l1, l2)
        #
        # return l1

        tmp1 = l1
        tmp2 = l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            ret = ListNode(l1.val)
            tmp1 = tmp1.next
        else:
            ret = ListNode(l2.val)
            tmp2 = tmp2.next
        tmp = ret

        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                tmp.next = ListNode(tmp1.val)
                tmp1 = tmp1.next
            else:
                tmp.next = ListNode(tmp2.val)
                tmp2 = tmp2.next
            tmp = tmp.next
        if tmp1 is None:
            tmp.next = tmp2
        else:
            tmp.next = tmp1
        return ret

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pass

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # part = None
        # tmp = head
        # while True:
        #     if tmp:
        #         tmp=tmp.next
        #         n-=1
        #     if n<0:
        #         part
        pass

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp0 = head.val
        tmp1 = head.next.val
        index = 0
        while True:
            if head:
                if index % 2 == 0:
                    ret0 = tmp0
                    ret0.next = ListNode(head.val)
                    tmp0 = ret0
                else:
                    ret1 = tmp1
                    ret1.next = ListNode(head.val)
                    tmp1 = ret1
                head = head.next
            else:
                pass
            index += 1


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
    # ss.reverseList(l1)
    # linkA = ListNode(1)
    # linkA.next = ListNode(2)
    # linkA.next.next = ListNode(4)
    # linkA.next.next.next = ListNode(6)
    # linkB = ListNode(6)
    # linkB.next = ListNode(21)
    # ss.mergeTwoLists(linkA, linkB)
    # ss.mergeTwoLists(None, None)
    # ss.mergeTwoLists(linkA, None)
    # print(linkA)
    # print(linkB)
    # q = list2link([1, 324, 543, 1, 6346, 1])
    # w = list2link([])
    # e = list2link([0, 1])
    # link2list(q)
    # link2list(w)
    # link2list(e)
