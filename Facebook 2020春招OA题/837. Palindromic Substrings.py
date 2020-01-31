class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, str):
        n = len(str)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        results = 0
        for i in range(n):
            for j in range(i + 1):
                if str[i] == str[j] and (i - j <= 2 or dp[j + 1][i - 1] == 1):
                    dp[j][i] = 1
                results += dp[j][i]

        return results
