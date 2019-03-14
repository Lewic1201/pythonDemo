from source.utils.decorators import print_cls


class Solution:
    @print_cls
    def searchMatrix(self, matrix, target):
        """
        搜索二维矩阵 II

        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        pass

    @print_cls
    def majorityElement(self, nums):
        """
        求众数(众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。)
        :type nums: List[int]
        :rtype: int
        """
        # maps = {}
        # maxs = [None, 0]
        # for i in nums:
        #     if i not in maps:
        #         maps[i] = 1
        #     else:
        #         maps[i] += 1
        # for j in maps:
        #     if maps[j] > maxs[1]:
        #         maxs[0], maxs[1] = j, maps[j]
        # else:
        #     if maxs[1] > (len(nums) / 2):
        #         return maxs[0]

        maps = {}
        for i in nums:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
            if maps[i] > (len(nums) / 2):
                return i


if __name__ == '__main__':
    ss = Solution()
    ss.majorityElement([3, 2, 3])
    ss.majorityElement([2, 2, 1, 1, 1, 2, 2])
