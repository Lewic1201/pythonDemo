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

    @print_cls
    def titleToNumber(self, s: str) -> int:
        """Excel表列序号"""
        # letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # maps = {letter[k]: k+1 for k in range(26)}
        # print(maps)

        # maps = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        #         'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
        #         'X': 24, 'Y': 25, 'Z': 26}
        # res = 0
        #
        # for i in range(len(s)):
        #     res = res * 26 + maps[s[i]]
        # return res

        res = 0
        for i in s:
            g = ord(i) - 64
            res = res * 26 + g
        return res



if __name__ == '__main__':
    ss = Solution()
    # ss.lengthOfLongestSubstring("abcabcbb")
    # ss.lengthOfLongestSubstring("")
    # ss.lengthOfLongestSubstring("b")
    # ss.lengthOfLongestSubstring("ab")
    # ss.lengthOfLongestSubstring("pwwkew")

    ss.titleToNumber('A')
    ss.titleToNumber('Z')
    ss.titleToNumber('AA')
    ss.titleToNumber('AB')
    ss.titleToNumber('ZY')
    ss.titleToNumber('AAA')
    ss.titleToNumber('AAB')
