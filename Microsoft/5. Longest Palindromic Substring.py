class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        start, end = 0, 0
        n = len(s)

        for i in range(n):
            left, right = i, i
            while 0 <= left and right < n:
                if s[left] != s[right]:
                    break
                if right - left + 1 > longest:
                    start, end = left, right
                    longest = right - left + 1
                left, right = left - 1, right + 1

            left, right = i - 1, i
            while 0 <= left and right < n:
                if s[left] != s[right]:
                    break
                if right - left + 1 > longest:
                    start, end = left, right
                    longest = right - left + 1
                left, right = left - 1, right + 1

        return s[start: end + 1]
