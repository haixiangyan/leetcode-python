class Solution:
    DX = [1, 0, -1, 0]
    DY = [0, 1, 0, -1]

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, row, col)
                    islands += 1

        return islands

    def dfs(self, grid, i, j, row, col):
        if not (0 <= i < row and 0 <= j < col and grid[i][j] == '1'):
            return

        grid[i][j] = '0'

        for delta in range(4):
            next_x, next_y = i + self.DX[delta], j + self.DY[delta]
            self.dfs(grid, next_x, next_y, row, col)
