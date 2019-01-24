from source.utils.decorators import print_cls


class Solution:
    """hash"""

    @print_cls
    def numJewelsInStones(self, J, S):
        """
        宝石与石头
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in J:
            for j in S:
                if i == j:
                    count += 1
        return count

    @print_cls
    def lengthOfLongestSubstring(self, s):
        """
        无重复字符的最长子串
        eg:
            "abcabcbb"
            3
        :type s: str
        :rtype: int
        """
        nums = 0
        slen = len(s)
        middle = ''
        if slen <= 1:
            return slen
        for i in range(slen):
            if s[i] in middle:
                if len(middle) > nums:
                    nums = len(middle)
                middle = middle[1:]
            middle += s[i]
        return nums


if __name__ == '__main__':
    ss = Solution()
    ss.lengthOfLongestSubstring("abcabcbb")
    ss.lengthOfLongestSubstring("")
    ss.lengthOfLongestSubstring("b")
    ss.lengthOfLongestSubstring("ab")
    ss.lengthOfLongestSubstring("pwwkew")
