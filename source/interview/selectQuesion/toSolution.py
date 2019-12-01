#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 23:56
# @Author  : Administrator
# @File    : toSolution.py
# @Software: PyCharm
# @context :
"""
试题题目文字版：

1.这道题的答案是

A.A B.B C.C D.D

2.第5题的答案是

A.C B.D C.A D.B

3.以下选项中哪一题的答案与其他三项不同

A.第3题B.第6题C.第2题D.第4题

4.以下选项中哪两题的答案相同

A.第1，5题B.第2，7题C.第1，9题D.第6，10题

5.以下选项中哪一题的答案与本题相同

A.第8题B.第4题C.第9题D.第7题

6.以下选项中哪两题的答案与第8题相同

A.第2，4题B.第1，6题C.第3，10题D.第5，9题

7.在此十道题中，被选择次数最少的选项字母为

A.C B.B C.A D.D

8.以下选项中哪一题的答案与第1题的答案在字母表中不相邻

A.第7题B.第5题C.第2题D.第10题

9.已知“第1题与第6题的答案相同”与“第X题与第5题的答案相同”的真假性相反，那么X为

A.第6题B.第10题C.第2题D.第9题

10.在此十道题中，ABCD四个字母中出现的次数最多者与最少者的差为

A.3 B.2 C.4 D.1

本试题的答案为______________。

"""

import sys
import itertools
from source.utils.decorators import times


# sys.setrecursionlimit(10000)

@times
def solution0():
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

    def Q1():
        options = {
            A: A,
            B: B,
            C: C,
            D: D,
        }
        option = options[answer[1]]
        return option == answer[1]

    def Q2():
        options = {
            A: C,
            B: D,
            C: A,
            D: B,
        }
        option = options[answer[2]]
        return option == answer[5]

    def Q3():
        options = {
            A: answer[3],
            B: answer[6],
            C: answer[2],
            D: answer[4],
        }
        option = options[answer[3]]
        values = list(options.values())
        values.remove(option)
        return option not in values

    def Q4():
        options = {
            A: (answer[1], answer[5]),
            B: (answer[2], answer[7]),
            C: (answer[1], answer[9]),
            D: (answer[6], answer[10]),
        }
        option = options[answer[4]]
        return option[0] == option[1]

    def Q5():
        options = {
            A: answer[8],
            B: answer[4],
            C: answer[9],
            D: answer[7],
        }
        option = options[answer[5]]
        return option == answer[5]

    def Q6():
        options = {
            A: (answer[2], answer[4]),
            B: (answer[1], answer[6]),
            C: (answer[3], answer[10]),
            D: (answer[5], answer[9]),
        }
        option = options[answer[6]]
        return len(set(list(option) + [answer[8]])) == 1

    def Q7():
        options = {
            A: answer.count(C),
            B: answer.count(B),
            C: answer.count(A),
            D: answer.count(D),
        }
        option = options[answer[7]]
        return option == min(options.values())

    def Q8():
        options = {
            A: answer[7],
            B: answer[5],
            C: answer[2],
            D: answer[10],
        }
        option = options[answer[8]]
        return abs(ord(option) - ord(answer[1])) != 1

    def Q9():
        options = {
            A: answer[6],
            B: answer[10],
            C: answer[2],
            D: answer[9],
        }
        option = options[answer[9]]
        assume1 = (answer[1] == answer[6])
        assume2 = (option == answer[5])
        return assume1 != assume2

    def Q10():
        options = {
            A: 3,
            B: 2,
            C: 4,
            D: 1,
        }
        option = options[answer[10]]
        keys = options.keys()
        counts = [answer.count(key) for key in keys]
        return option == abs(max(counts) - min(counts))

    # 获取10道题答案的全排列
    answers = itertools.product([A, B, C, D], repeat=10)
    for answer in answers:
        # 为了让代码更容易看懂，加了个下标占位符
        answer = [''] + list(answer)
        if Q1() and Q2() and Q3() and Q4() and Q5() and \
                Q6() and Q7() and Q8() and Q9() and Q10():
            ret = (''.join(answer))
            return ret


def solution1():
    res = []

    def select(group):
        num = 9
        for i in range(len(group)):
            if not group[i]:
                num = i
                break
        else:

            # 第七题
            numA = group.count('a')
            numB = group.count('b')
            numC = group.count('c')
            numD = group.count('d')
            sorts = sorted([numA, numB, numC, numD])
            if group[6] == 'a' and sorts[0] != numA:
                return
            elif group[6] == 'b' and sorts[0] != numB:
                return
            elif group[6] == 'c' and sorts[0] != numC:
                return
            elif group[6] == 'd' and sorts[0] != numD:
                return

            # 第十题
            cha = sorts[3] - sorts[0]

            if group[9] == 'a' and cha != 3:
                return
            elif group[9] == 'b' and cha != 2:
                return
            elif group[9] == 'c' and cha != 4:
                return
            elif group[9] == 'd' and cha != 1:
                return

            # 返回答案
            res.append(group)

        # 第二题确定
        if num == 4:
            if group[1] == 'a':
                group[4] = 'c'
            elif group[1] == 'b':
                group[4] = 'd'
            elif group[1] == 'c':
                group[4] = 'a'
            elif group[1] == 'd':
                group[4] = 'b'

        # 第五题确定
        if group[4] == 'a':
            if group[7] == 0:
                group[7] = 'a'
            elif group[7] != 'a' and group[3] == 'b' and group[8] == 'c' and group[6] == 'd':
                return
        elif group[4] == 'b':
            if group[3] == 0:
                group[3] = 'b'
            elif group[7] == 'a' and group[3] != 'b' and group[8] == 'c' and group[6] == 'd':
                return
        elif group[4] == 'c':
            if group[8] == 0:
                group[8] = 'c'
            elif group[7] == 'a' and group[3] == 'b' and group[8] != 'c' and group[6] == 'd':
                return
        elif group[4] == 'd':
            if group[6] == 0:
                group[6] = 'd'
            elif group[7] == 'a' and group[3] == 'b' and group[8] == 'c' and group[6] != 'd':
                return

        # 第三题
        if group[2] == 'a':
            if group[5] == group[2] or group[1] == group[2] or group[3] == group[2]:
                return
        elif group[2] == 'b':
            if group[2] == group[5] or group[1] == group[5] or group[3] == group[5]:
                return
        elif group[2] == 'c':
            if group[2] == group[1] or group[5] == group[1] or group[3] == group[1]:
                return
        elif group[2] == 'd':
            if group[2] == group[3] or group[5] == group[3] or group[1] == group[3]:
                return

        # 第四题
        if group[3] == 'a':
            if group[0] and group[4] and group[0] != group[4]:
                return
            if group[1] and group[6] and group[1] == group[6]:
                return
            if group[0] and group[8] and group[0] == group[8]:
                return
            if group[5] and group[9] and group[5] == group[9]:
                return
        elif group[3] == 'b':
            if group[0] and group[4] and group[0] == group[4]:
                return
            if group[1] and group[6] and group[1] != group[6]:
                return
            if group[0] and group[8] and group[0] == group[8]:
                return
            if group[5] and group[9] and group[5] == group[9]:
                return
        elif group[3] == 'c':
            if group[0] and group[4] and group[0] == group[4]:
                return
            if group[1] and group[6] and group[1] == group[6]:
                return
            if group[0] and group[8] and group[0] != group[8]:
                return
            if group[5] and group[9] and group[5] == group[9]:
                return
        elif group[3] == 'd':
            if group[0] and group[4] and group[0] == group[4]:
                return
            if group[1] and group[6] and group[1] == group[6]:
                return
            if group[0] and group[8] and group[0] == group[8]:
                return
            if group[5] and group[9] and group[5] != group[9]:
                return

        # 第六题
        if group[7]:
            if group[5] == 'a':
                if (group[1] and group[1] != group[7]) or (group[3] and group[3] != group[7]):
                    return
                if group[0] and group[5] and group[0] == group[5] == group[7]:
                    return
                if group[2] and group[9] and group[2] == group[9] == group[7]:
                    return
                if group[4] and group[8] and group[4] == group[8] == group[7]:
                    return
            elif group[2] == 'b':
                if group[1] and group[3] and group[1] == group[3] == group[7]:
                    return
                if (group[0] and group[0] != group[7]) or (group[5] and group[5] != group[7]):
                    return
                if group[2] and group[9] and group[2] == group[9] == group[7]:
                    return
                if group[4] and group[8] and group[4] == group[8] == group[7]:
                    return
            elif group[2] == 'c':
                if group[1] and group[3] and group[1] == group[3] == group[7]:
                    return
                if group[0] and group[5] and group[0] == group[5] == group[7]:
                    return
                if (group[2] and group[2] != group[7]) or (group[9] and group[9] != group[7]):
                    return
                if group[4] and group[8] and group[4] == group[8] == group[7]:
                    return
            elif group[2] == 'd':
                if group[1] and group[3] and group[1] == group[3] == group[7]:
                    return
                if group[0] and group[5] and group[0] == group[5] == group[7]:
                    return
                if group[2] and group[9] and group[2] == group[9] == group[7]:
                    return
                if (group[4] and group[4] != group[7]) or (group[8] and group[8] != group[7]):
                    return

        # 第八题
        def border(let1, let2):
            ret = let1 + let2
            if ret in ['ab', 'bc', 'cd', 'ba', 'cb', 'dc']:
                return True
            elif ret in ['ac', 'bd', 'ca', 'db', 'ad', 'da']:
                return False

        if group[0]:
            if group[7] == 'a':
                if group[6] and border(group[0], group[6]):
                    return
                if group[4] and not border(group[0], group[4]):
                    return
                if group[1] and not border(group[0], group[1]):
                    return
                if group[9] and not border(group[0], group[9]):
                    return
            elif group[7] == 'b':
                if group[6] and not border(group[0], group[6]):
                    return
                if group[4] and border(group[0], group[4]):
                    return
                if group[1] and not border(group[0], group[1]):
                    return
                if group[9] and not border(group[0], group[9]):
                    return
            elif group[7] == 'c':
                if group[6] and not border(group[0], group[6]):
                    return
                if group[4] and not border(group[0], group[4]):
                    return
                if group[1] and border(group[0], group[1]):
                    return
                if group[9] and not border(group[0], group[9]):
                    return
            elif group[7] == 'd':
                if group[6] and not border(group[0], group[6]):
                    return
                if group[4] and not border(group[0], group[4]):
                    return
                if group[1] and not border(group[0], group[1]):
                    return
                if group[9] and border(group[0], group[9]):
                    return

        # 第九题
        if group[0] and group[5] and group[4]:
            flag16 = not (group[0] == group[5])
            if group[8] == 'a':
                if group[5]:
                    if (not flag16) == (group[4] == group[5]):
                        return
                if group[9]:
                    if flag16 == (group[4] == group[9]):
                        return
                if group[1]:
                    if flag16 == (group[4] == group[1]):
                        return
                if group[8]:
                    if flag16 == (group[4] == group[8]):
                        return
            elif group[8] == 'b':
                if group[5]:
                    if flag16 == (group[4] == group[5]):
                        return
                if group[9]:
                    if (not flag16) == (group[4] == group[9]):
                        return
                if group[1]:
                    if flag16 == (group[4] == group[1]):
                        return
                if group[8]:
                    if flag16 == (group[4] == group[8]):
                        return
            elif group[8] == 'c':
                if group[5]:
                    if flag16 == (group[4] == group[5]):
                        return
                if group[9]:
                    if flag16 == (group[4] == group[9]):
                        return
                if group[1]:
                    if (not flag16) == (group[4] == group[1]):
                        return
                if group[8]:
                    if flag16 == (group[4] == group[8]):
                        return
            elif group[8] == 'd':
                if group[5]:
                    if flag16 == (group[4] == group[5]):
                        return
                if group[9]:
                    if flag16 == (group[4] == group[9]):
                        return
                if group[1]:
                    if flag16 == (group[4] == group[1]):
                        return
                if group[8]:
                    if (not flag16) == (group[4] == group[8]):
                        return

        if group[num] == 0:
            group1 = group[:]
            group2 = group[:]
            group3 = group[:]
            group4 = group[:]
            group1[num] = 'a'
            group2[num] = 'b'
            group3[num] = 'c'
            group4[num] = 'd'
            return select(group1), select(group2), select(group3), select(group4)
        else:
            return select(group)

    select([0 for i in range(10)])
    return res


@times
def solution2():
    options = [i for i in 'abcd']
    res = []

    for i1 in options:
        for i2 in options:
            for i3 in options:
                for i4 in options:
                    for i5 in options:
                        for i6 in options:
                            for i7 in options:
                                for i8 in options:
                                    for i9 in options:
                                        for i10 in options:
                                            group = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
                                            if check(group):
                                                # if check_simple(group):
                                                res.append(group)

    return res


def check(group):
    # 第七题
    numA = group.count('a')
    numB = group.count('b')
    numC = group.count('c')
    numD = group.count('d')
    sorts = sorted([numA, numB, numC, numD])
    if group[6] == 'a' and sorts[0] != numA:
        return
    elif group[6] == 'b' and sorts[0] != numB:
        return
    elif group[6] == 'c' and sorts[0] != numC:
        return
    elif group[6] == 'd' and sorts[0] != numD:
        return

    # 第十题
    cha = sorts[3] - sorts[0]
    if group[9] == 'a' and cha != 3:
        return
    elif group[9] == 'b' and cha != 2:
        return
    elif group[9] == 'c' and cha != 4:
        return
    elif group[9] == 'd' and cha != 1:
        return

    # 第二题确定
    if group[1] == 'a' and group[4] != 'c':
        return
    elif group[1] == 'b' and group[4] != 'd':
        return
    elif group[1] == 'c' and group[4] != 'a':
        return
    elif group[1] == 'd' and group[4] != 'b':
        return

    # 第五题确定
    if group[4] == 'a':
        if group[7] != 'a' and group[3] == 'b' and group[8] == 'c' and group[6] == 'd':
            return
    elif group[4] == 'b':
        if group[7] == 'a' and group[3] != 'b' and group[8] == 'c' and group[6] == 'd':
            return
    elif group[4] == 'c':
        if group[7] == 'a' and group[3] == 'b' and group[8] != 'c' and group[6] == 'd':
            return
    elif group[4] == 'd':
        if group[7] == 'a' and group[3] == 'b' and group[8] == 'c' and group[6] != 'd':
            return

    # 第三题
    if group[2] == 'a':
        if group[5] == group[2] or group[1] == group[2] or group[3] == group[2]:
            return
    elif group[2] == 'b':
        if group[2] == group[5] or group[1] == group[5] or group[3] == group[5]:
            return
    elif group[2] == 'c':
        if group[2] == group[1] or group[5] == group[1] or group[3] == group[1]:
            return
    elif group[2] == 'd':
        if group[2] == group[3] or group[5] == group[3] or group[1] == group[3]:
            return

    # 第四题
    if group[3] == 'a':
        if group[0] != group[4]:
            return
        if group[1] == group[6]:
            return
        if group[0] == group[8]:
            return
        if group[5] == group[9]:
            return
    elif group[3] == 'b':
        if group[0] == group[4]:
            return
        if group[1] != group[6]:
            return
        if group[0] == group[8]:
            return
        if group[5] == group[9]:
            return
    elif group[3] == 'c':
        if group[0] == group[4]:
            return
        if group[1] == group[6]:
            return
        if group[0] != group[8]:
            return
        if group[5] == group[9]:
            return
    elif group[3] == 'd':
        if group[0] == group[4]:
            return
        if group[1] == group[6]:
            return
        if group[0] == group[8]:
            return
        if group[5] != group[9]:
            return

    # 第六题
    if group[5] == 'a':
        if (group[1] != group[7]) or (group[3] != group[7]):
            return
        if group[0] == group[5] == group[7]:
            return
        if group[2] == group[9] == group[7]:
            return
        if group[4] == group[8] == group[7]:
            return
    elif group[5] == 'b':
        if group[1] == group[3] == group[7]:
            return
        if (group[0] != group[7]) or (group[5] != group[7]):
            return
        if group[2] == group[9] == group[7]:
            return
        if group[4] == group[8] == group[7]:
            return
    elif group[5] == 'c':
        if group[1] == group[3] == group[7]:
            return
        if group[0] == group[5] == group[7]:
            return
        if (group[9] != group[7]) or (group[9] != group[7]):
            return
        if group[4] == group[8] == group[7]:
            return
    elif group[5] == 'd':
        if group[1] == group[3] == group[7]:
            return
        if group[0] == group[5] == group[7]:
            return
        if group[2] == group[9] == group[7]:
            return
        if (group[4] != group[7]) or (group[8] != group[7]):
            return

    # 第八题
    def border(let1, let2):
        ret = let1 + let2
        if ret in ['ab', 'bc', 'cd', 'ba', 'cb', 'dc']:
            return True
        elif ret in ['ac', 'bd', 'ca', 'db', 'ad', 'da']:
            return False

    if group[7] == 'a':
        if group[6] and border(group[0], group[6]):
            return
        if group[4] and not border(group[0], group[4]):
            return
        if group[1] and not border(group[0], group[1]):
            return
        if group[9] and not border(group[0], group[9]):
            return
    elif group[7] == 'b':
        if group[6] and not border(group[0], group[6]):
            return
        if group[4] and border(group[0], group[4]):
            return
        if group[1] and not border(group[0], group[1]):
            return
        if group[9] and not border(group[0], group[9]):
            return
    elif group[7] == 'c':
        if group[6] and not border(group[0], group[6]):
            return
        if group[4] and not border(group[0], group[4]):
            return
        if group[1] and border(group[0], group[1]):
            return
        if group[9] and not border(group[0], group[9]):
            return
    elif group[7] == 'd':
        if group[6] and not border(group[0], group[6]):
            return
        if group[4] and not border(group[0], group[4]):
            return
        if group[1] and not border(group[0], group[1]):
            return
        if group[9] and border(group[0], group[9]):
            return

    # 第九题
    flag16 = (group[0] == group[5])
    if group[8] == 'a':
        if flag16 == (group[4] == group[5]):
            return
        if flag16 != (group[4] == group[9]):
            return
        if flag16 != (group[4] == group[1]):
            return
        if flag16 != (group[4] == group[8]):
            return
    elif group[8] == 'b':
        if flag16 != (group[4] == group[5]):
            return
        if flag16 == (group[4] == group[9]):
            return
        if flag16 != (group[4] == group[1]):
            return
        if flag16 != (group[4] == group[8]):
            return
    elif group[8] == 'c':
        if flag16 != (group[4] == group[5]):
            return
        if flag16 != (group[4] == group[9]):
            return
        if flag16 == (group[4] == group[1]):
            return
        if flag16 != (group[4] == group[8]):
            return
    elif group[8] == 'd':
        if flag16 != (group[4] == group[5]):
            return
        if flag16 != (group[4] == group[9]):
            return
        if flag16 != (group[4] == group[1]):
            return
        if flag16 == (group[4] == group[8]):
            return

    return True


def check_simple(group):
    # 第七题
    numA = group.count('a')
    numB = group.count('b')
    numC = group.count('c')
    numD = group.count('d')
    sorts = sorted([numA, numB, numC, numD])
    if group[6] == 'a' and sorts[0] != numA:
        return
    elif group[6] == 'b' and sorts[0] != numB:
        return
    elif group[6] == 'c' and sorts[0] != numC:
        return
    elif group[6] == 'd' and sorts[0] != numD:
        return

    # 第十题
    cha = sorts[3] - sorts[0]
    if group[9] == 'a' and cha != 3:
        return
    elif group[9] == 'b' and cha != 2:
        return
    elif group[9] == 'c' and cha != 4:
        return
    elif group[9] == 'd' and cha != 1:
        return

    # 第二题确定
    if group[1] == 'a' and group[4] != 'c':
        return
    elif group[1] == 'b' and group[4] != 'd':
        return
    elif group[1] == 'c' and group[4] != 'a':
        return
    elif group[1] == 'd' and group[4] != 'b':
        return

    # 第五题确定
    if group[4] == 'a':
        if group[7] != 'a':
            return
    elif group[4] == 'b':
        if group[7] == 'a':
            return
    elif group[4] == 'c':
        if group[7] == 'a':
            return
    elif group[4] == 'd':
        if group[7] == 'a':
            return

    # 第三题
    if group[2] == 'a':
        if group[5] == group[2] or group[1] == group[2] or group[3] == group[2]:
            return
    elif group[2] == 'b':
        if group[2] == group[5] or group[1] == group[5] or group[3] == group[5]:
            return
    elif group[2] == 'c':
        if group[2] == group[1] or group[5] == group[1] or group[3] == group[1]:
            return
    elif group[2] == 'd':
        if group[2] == group[3] or group[5] == group[3] or group[1] == group[3]:
            return

    # 第四题
    if group[3] == 'a':
        if group[0] != group[4]:
            return
    elif group[3] == 'b':
        if group[0] == group[4]:
            return
    elif group[3] == 'c':
        if group[0] == group[4]:
            return
    elif group[3] == 'd':
        if group[0] == group[4]:
            return
    # 第六题
    if group[5] == 'a':
        if (group[1] != group[7]) or (group[3] != group[7]):
            return
    elif group[5] == 'b':
        if (group[0] != group[7]) or (group[5] != group[7]):
            return
    elif group[5] == 'c':
        if (group[9] != group[7]) or (group[9] != group[7]):
            return
    elif group[5] == 'd':
        if (group[4] != group[7]) or (group[8] != group[7]):
            return

    # 第八题
    def border(let1, let2):
        ret = let1 + let2
        if ret in ['ab', 'bc', 'cd', 'ba', 'cb', 'dc']:
            return True
        elif ret in ['ac', 'bd', 'ca', 'db', 'ad', 'da']:
            return False

    if group[7] == 'a':
        if group[6] and border(group[0], group[6]):
            return
    elif group[7] == 'b':
        if group[4] and border(group[0], group[4]):
            return
    elif group[7] == 'c':
        if group[1] and border(group[0], group[1]):
            return
    elif group[7] == 'd':
        if group[9] and border(group[0], group[9]):
            return

    # 第九题
    flag16 = (group[0] == group[5])
    if group[8] == 'a':
        if flag16 == (group[4] == group[5]):
            return
    elif group[8] == 'b':
        if flag16 == (group[4] == group[9]):
            return
    elif group[8] == 'c':
        if flag16 == (group[4] == group[1]):
            return
    elif group[8] == 'd':
        if flag16 == (group[4] == group[8]):
            return

    return True


if __name__ == '__main__':
    # 可行方案 solution0(),solution2()
    print(solution0())
    print(solution2())
    # print(check('bcacacdaba'))
