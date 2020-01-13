class Solution:
    def __init__(self):
        self.paths = 0
        self.visited = []
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param m: the row
    @param n: the column
    @return: the possible unique paths
    """
    def uniquePaths(self, m, n):
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.visited[0][0] = True

        self.dfs(0, 0, m, n)

        return self.paths

    def dfs(self, x, y, m, n):
        if x == m - 1 and y == n - 1:
            self.paths += 1
            return

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]

            if 0 <= next_x < m and 0 <= next_y < n and not self.visited[next_x][next_y]:
                self.visited[next_x][next_y] = True
                self.dfs(next_x, next_y, m, n)
                self.visited[next_x][next_y] = False
