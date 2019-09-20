class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """

    def countPalindromicSubstrings(self, str):
        # write your code here
        dp = [[0 for j in range(len(str))] for i in range(len(str))]
        ans = 0
        for i in range(len(str)):
            for j in range(i + 1):
                if str[j] == str[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1):
                    dp[j][i] = 1
                ans += dp[j][i]
        return ans
