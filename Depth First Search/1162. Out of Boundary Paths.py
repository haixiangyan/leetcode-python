class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param m: an integer
    @param n: an integer
    @param N: an integer
    @param i: an integer
    @param j: an integer
    @return: the number of paths to move the ball out of grid boundary
    """
    def findPaths(self, m, n, N, i, j):
        if N == 0:
            return 0

        result = self.dfs(N, {}, 0, m, n, i, j)

        return result % (10 ** 9 + 7)

    def dfs(self, N, memo, steps, rows, cols, x, y):
        if (x, y, steps) in memo:
            return memo[(x, y, steps)]

        if not (0 <= x < rows and 0 <= y < cols):
            return 1
        if steps == N:
            return 0

        paths = 0
        for delta in range(4):
            paths += self.dfs(N, memo, steps + 1, rows, cols, x + self.dx[delta], y + self.dy[delta])
        memo[(x, y, steps)] = paths
        return paths
