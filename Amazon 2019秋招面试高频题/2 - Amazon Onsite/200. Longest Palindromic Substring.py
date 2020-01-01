class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ''

        longest = ''
        max_length = 0

        for i in range(len(s)):
            # Check if it's palindromic string
            curt_longest = self.check(s, i)

            if max_length < len(curt_longest):
                max_length = len(curt_longest)
                longest = curt_longest

        return longest

    def check(self, s, i):
        left, right = i, i

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left, right = left - 1, right + 1

        curt_longest = s[left + 1:right]

        left, right = i, i + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left, right = left - 1, right + 1

        return curt_longest if len(curt_longest) > right - left - 1 else s[left + 1:right]
