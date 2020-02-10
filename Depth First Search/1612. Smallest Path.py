class Solution:
    """
    @param matrix:
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dp[0][j] = matrix[i][j]
                else:
                    if j - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                    if j + 1 < cols:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][j]) + matrix[i][j]

        return min(dp[-1])
