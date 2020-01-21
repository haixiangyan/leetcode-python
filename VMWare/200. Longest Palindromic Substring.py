class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return s

        length = len(s)
        longest = 0
        longest_str = ''

        for i in range(length):
            # aba
            left, right = i, i
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                if longest < right - left + 1:
                    longest = right - left + 1
                    longest_str = s[left:right + 1]
                left -= 1
                right += 1

            # abba
            left, right = i, i + 1
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                if longest < right - left + 1:
                    longest = right - left + 1
                    longest_str = s[left:right + 1]
                left -= 1
                right += 1

        return longest_str
