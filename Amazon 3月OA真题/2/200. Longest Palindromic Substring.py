class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if s == '':
            return ''

        longestLen = 0
        longestStr = ''
        n = len(s)

        for index, char in enumerate(s):
            # 'abcba'
            left, right = index, index
            while 0 <= left and right < n:
                if s[left] != s[right]:
                    break
                if right - left + 1 > longestLen:
                    longestLen = right - left + 1
                    longestStr = s[left:right + 1]

                left -= 1
                right += 1

            # 'abba'
            left, right = index, index + 1
            while 0 <= left and right < n:
                if s[left] != s[right]:
                    break
                if right - left + 1 > longestLen:
                    longestLen = right - left + 1
                    longestStr = s[left:right + 1]

                left -= 1
                right += 1

        return longestStr
