from collections import deque


class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """

    def numsofIsland(self, grid, k):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = self.bfs(grid, i, j)
                    if size >= k:
                        islands += 1

        return islands

    def bfs(self, grid, x, y):
        size = 0
        queue = deque([(x, y)])
        grid[x][y] = 0

        while queue:
            size += 1
            x, y = queue.popleft()

            for delta in range(4):
                next_x, next_y = x + self.dx[delta], y + self.dy[delta]
                if self.is_valid(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = 0

        return size

    def is_valid(self, grid, next_x, next_y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == 1
