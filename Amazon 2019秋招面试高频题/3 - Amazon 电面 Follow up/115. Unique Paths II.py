class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = obstacleGrid

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    dp[i][j] = 1 - dp[i][j]
                elif i == 0:
                    dp[i][j] = 0 if dp[i][j] == 1 else dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = 0 if dp[i][j] == 1 else dp[i - 1][j]
                else:
                    dp[i][j] = 0 if dp[i][j] == 1 else dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
