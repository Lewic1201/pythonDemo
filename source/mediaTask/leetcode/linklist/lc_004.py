from functools import wraps


def prints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("FUNCTION: {func}()".format(func=func.__name__))
        print('PARAMS  : %s,%s' % (args[1:], kwargs))
        ret = func(*args, **kwargs)
        print("RESULT  : {ret}".format(ret=ret))
        return ret

    return wrapper


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '{}->{}'.format(self.val, str(self.next))


class Solution(object):

    def __init__(self):
        pass

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


if __name__ == '__main__':
    ss = Solution()
    linkA = ListNode(1)
    linkA.next = ListNode(2)
    linkA.next.next = ListNode(4)
    linkA.next.next.next = ListNode(6)
    linkB = ListNode(6)
    linkB.next = ListNode(21)
    ss.mergeTwoLists(linkA, linkB)
    # ss.mergeTwoLists(None, None)
    # ss.mergeTwoLists(linkA, None)
    # print(linkA)
    # print(linkB)
