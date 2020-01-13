class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[set() for _ in range(cols)] for _ in range(rows)]

        if rows == 0 or cols == 0:
            return 0

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    dp[i][j].add(grid[i][j])
                else:
                    for value in dp[i - 1][j]:
                        dp[i][j].add(value + grid[i][j])
                    for value in dp[i][j - 1]:
                        dp[i][j].add(value + grid[i][j])

        weights = 0
        for value in dp[-1][-1]:
            weights += value

        return weights
