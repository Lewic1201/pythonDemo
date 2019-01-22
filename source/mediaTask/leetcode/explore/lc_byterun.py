from source.utils.decorators import print_cls


class Solution:
    """字节跳动练习"""

    @print_cls
    def findCircleNum(self, M):
        """
        朋友圈
        :type M: List[List[int]]
        :rtype: int
        """
        """
        [[1,2,0,0],
         [1,2,0,4],
         [0,0,3,0],
         [0,2,0,4]]
 
        2
        """
        mlen = len(M)
        group = set()
        # ret = []
        # for i in range(mlen):
        #     if M[0][i]:
        #         group.add(i)
        #     for i in group
        def find_mb(M,i,group):
            tmp = M[i]
            for p in range(mlen):
                if M[i][p]==1:
                    group.add(p)



if __name__ == '__main__':
    ss = Solution()
