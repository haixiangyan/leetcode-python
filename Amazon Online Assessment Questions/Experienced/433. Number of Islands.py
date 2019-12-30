from collections import deque

class Solution:
    def __init__(self):
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    islands += 1

        return islands

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            grid[x][y] = 0

            for delta in range(4):
                next_x, next_y = x + self.dx[delta], y + self.dy[delta]
                if self.is_in_bound(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = 0

    def is_in_bound(self, grid, x, y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1
