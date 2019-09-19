class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = 1
                # 第一行
                elif i == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i][j - 1]
                # 第一列
                elif j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows - 1][cols - 1]
