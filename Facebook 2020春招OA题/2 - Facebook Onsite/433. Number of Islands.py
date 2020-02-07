class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.dfs(grid, i, j, rows, cols)
                    islands += 1

        return islands

    def dfs(self, grid, x, y, rows, cols):
        if not (0 <= x < rows and 0 <= y < cols) or not grid[x][y]:
            return

        grid[x][y] = False
        for delta in range(4):
            self.dfs(grid, x + self.dx[delta], y + self.dy[delta], rows, cols)
