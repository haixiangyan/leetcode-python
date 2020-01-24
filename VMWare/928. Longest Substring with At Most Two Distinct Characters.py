class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        most_right = {}
        l, r = 0, 0
        longest = 0

        while r < len(s):
            if len(most_right) <= 2:
                most_right[s[r]] = r
                r += 1
            if len(most_right) > 2:
                left = len(s)
                # Find most left
                for value in most_right.values():
                    left = min(left, value)
                most_right.pop(s[left])
                l = left + 1
            longest = max(longest, r - l)

        return longest
