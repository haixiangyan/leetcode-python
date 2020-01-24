class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        longest = 0
        l, r = 0, 0
        most_right = {}

        while r < len(s):
            if len(most_right) <= k:
                most_right[s[r]] = r
                r += 1
            if len(most_right) > k:
                left = len(s)
                for value in most_right.values():
                    left = min(left, value)
                l = left + 1
            longest = max(longest, l - r)

        return longest
