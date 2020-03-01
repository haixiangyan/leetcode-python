class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def maxAreaOfIsland(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area = max(area, self.dfs(grid, i, j, rows, cols, 1))

        return area

    def dfs(self, grid, x, y, rows, cols, area):
        grid[x][y] = 0

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]
            if not (0 <= next_x < rows and 0 <= next_y < cols) or grid[next_x][next_y] == 0:
                continue
            area = 1 + self.dfs(grid, next_x, next_y, rows, cols, area)

        return area
