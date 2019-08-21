class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = {}
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] = dp[(i, j - 1)] + dp[(i - 1, j)]

        return dp[(m - 1, n - 1)]
