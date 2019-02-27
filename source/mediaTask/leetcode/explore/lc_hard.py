from source.utils.decorators import print_cls
from source.utils.decorators import print_def
from source.utils.decorators import times
import pprint
import copy


class Solution:
    """难度: 困难"""

    @times
    @print_cls
    def solveNQueens(self, n: int) -> [[str]]:
        """
        N皇后问题:
        n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        """
        # 初始化棋盘
        mod = ['.' * n for _ in range(n)]

        ret = []

        def judge(mod, i, j):
            """判断当前位置是否可放置皇后"""
            for row in range(n):
                for col in range(n):
                    if row >= i and col >= j:
                        # 只判断之前的值
                        # continue
                        return True
                    if mod[row][col] == 'Q':
                        # 横竖斜校验
                        if row == i or col == j or row + col == i + j or row - col == i - j:
                            return False

        def judge2(mod, i, j):
            flag = 0
            for row in range(n):
                for col in range(n):
                    if row >= i and col >= j:
                        # 只判断之前的值
                        # continue
                        if flag > 0:
                            return False
                        return True
                    if mod[row][col] == 'Q':
                        # 横竖斜校验
                        if row == i:
                            flag += 1
                        elif col == j:
                            flag += 1
                        elif row + col == i + j:
                            flag += 1
                        elif row - col == i - j:
                            flag += 1
                    if flag == 4:
                        return 'EXIT'

        def inner(mod, index, count):
            """
            下棋
            :param mod: 棋盘
            :param index: 位置
            :param count: 已下的棋的个数
            :return:
            """
            p = index // n
            q = index % n
            if index > n * n:
                # ret.append(mod)
                if count == n:
                    ret.append(mod)
                return
            elif index > n * n // 2:
                tmp = judge2(mod, p, q)
                if tmp == 'EXIT':
                    return
                elif tmp is True:
                    # 如果该位置可行,分两种情况递归
                    mod2 = mod[:]
                    mod2[p] = q * '.' + 'Q' + (n - q - 1) * '.'
                    return inner(mod, index + 1, count), inner(mod2, index + 1, count + 1)
                else:
                    return inner(mod, index + 1, count)
            else:
                if judge(mod, p, q):
                    # 如果该位置可行,分两种情况递归
                    mod2 = mod[:]
                    mod2[p] = q * '.' + 'Q' + (n - q - 1) * '.'
                    return inner(mod, index + 1, count), inner(mod2, index + 1, count + 1)
                else:
                    return inner(mod, index + 1, count)

        inner(mod, 0, 0)
        return ret

    @print_cls
    @times
    def solveNQueens0(self, n: int) -> [[str]]:
        """
        N皇后问题:
        n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        """
        # 初始化棋盘
        mod = [[1 for _ in range(n)] for _ in range(n)]

        ret = []

        def judge(mod, i, j):
            """判断当前位置是否可放置皇后"""
            for row in range(n):
                for col in range(n):
                    if row >= i and col >= j:
                        # 只判断之前的值
                        # continue
                        return True
                    if mod[row][col] == 8:
                        # 横竖斜校验
                        if row == i or col == j or row + col == i + j or row - col == i - j:
                            return False

        def inner(mod, index, count):
            """
            下棋
            :param mod: 棋盘
            :param index: 位置
            :param count: 已下的棋的个数
            :return:
            """
            p = index // n
            q = index % n
            if index > n * n:
                # ret.append(mod)
                if count == n:
                    ret.append(mod)
                return
            if judge(mod, p, q):
                # 如果该位置可行,分两种情况递归
                mod2 = copy.deepcopy(mod)
                mod2[p][q] = 8
                return inner(mod, index + 1, count), inner(mod2, index + 1, count + 1)
            else:
                return inner(mod, index + 1, count)

        inner(mod, 0, 0)
        return ret

    @print_cls
    @times
    def solveNQueens1(self, n: int) -> [[str]]:
        mod = [[1 for _ in range(n)] for _ in range(n)]
        ret = []

        def nexts(mod, i, j, count):
            index = i * n + j
            if index > n * n:
                # ret.append(mod)
                if count == n:
                    ret.append(mod)
                return

            # 判断下一步
            for row in range(n):
                for col in range(n):
                    if row >= i and col >= j:
                        mod2 = copy.deepcopy(mod)
                        mod2[i][j] = 8
                        return nexts(mod, i, j + 1, count), nexts(mod2, i, j + 1, count + 1)

                    if mod[row][col] == 'Q':
                        # 横竖斜校验
                        if row == i:
                            if i < n - 1:
                                return nexts(mod, i + 1, 0, count)
                            else:
                                return
                        elif col == j:
                            return nexts(mod, i + 1, 0, count)
                        elif row + col == i + j:
                            nexts(mod, i, j + 1, count)
                        elif row - col == i - j:
                            nexts(mod, i, j + 1, count)

        return ret


if __name__ == '__main__':
    ss = Solution()
    ss.solveNQueens0(4)
    ss.solveNQueens(4)
