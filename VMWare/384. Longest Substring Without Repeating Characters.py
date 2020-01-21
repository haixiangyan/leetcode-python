class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        cache = {}
        left, right, longest = 0, 0, 0

        for right in range(len(s)):
            if s[right] in cache:
                left = max(left, cache[s[right]] + 1)

            longest = max(longest, right - left + 1)

            cache[s[right]] = right

        return longest
