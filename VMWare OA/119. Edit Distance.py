class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]
