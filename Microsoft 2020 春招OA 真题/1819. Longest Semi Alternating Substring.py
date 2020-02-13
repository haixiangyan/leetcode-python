class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # write your code here
        if len(s) < 3:
            return len(s)
        cnt = 1
        l = 0
        last = 0
        res = 0
        for r in range(1, len(s), 1):
            if s[r - 1] == s[r]:
                cnt = cnt + 1
            else:
                cnt = 1
                last = r
            if cnt > 2 and l < last:
                l = last
            while cnt > 2:
                l = l + 1
                cnt = cnt - 1
            res = max(res, r - l + 1)
        return res