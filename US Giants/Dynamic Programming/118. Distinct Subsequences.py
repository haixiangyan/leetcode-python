class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        n, m = len(S), len(T)

        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n):
            for j in range(m):
                if S[i] == T[j]:
                    dp[i + 1][j + 1] += dp[i][j]

                dp[i + 1][j + 1] += dp[i][j + 1]

        return dp[n][m]
