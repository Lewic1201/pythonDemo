from source.utils.decorators import print_cls
from source.utils.decorators import times


class Solution:
    """难度: 困难"""

    @print_cls
    @times
    def solveNQueens1(self, n: int) -> [[str]]:
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
            else:
                if judge(mod, p, q):
                    # 如果该位置可行,分两种情况递归
                    mod2 = mod[:]
                    mod2[p] = q * '.' + 'Q' + (n - q - 1) * '.'
                    return inner(mod, index + 1, count), inner(mod2, index + 1, count + 1)
                else:
                    return inner(mod, index + 1, count)

        inner(mod, 0, 0)
        return len(ret), ret

    @times
    @print_cls
    def solveNQueens(self, n: int) -> [[str]]:
        """
        n皇后
        """
        res = []
        ls = [0] * n

        def inner(row=0):
            if row == n:
                res.append(ls[:])
            for j in range(n):
                for i in range(row):
                    if ls[i] == j or ls[i] + i == j + row or ls[i] - i == j - row:
                        break
                else:
                    ls[row] = j
                    inner(row + 1)

        inner()
        for a in range(len(res)):
            res[a] = [('.' * j) + 'Q' + ('.' * (n - 1 - j)) for j in res[a]]
        return res


if __name__ == '__main__':
    ss = Solution()
    n = 9
    ss.solveNQueens(n)
    # ss.solveNQueens1(n)
