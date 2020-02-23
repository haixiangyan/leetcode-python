class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, rows, cols)
                    islands += 1
        return islands

    def dfs(self, grid, x, y, rows, cols):
        if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == '0':
            return

        grid[x][y] = '0'

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]
            self.dfs(grid, next_x, next_y, rows, cols)
