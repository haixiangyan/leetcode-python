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
                    size = self.bfs(grid, i, j, rows, cols)
                    print(size)
                    islands += 1 if size >= k else 0
        return islands

    def bfs(self, grid, x, y, rows, cols):
        area = 0
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            grid[x][y] = 0
            area += 1
            for delta in range(4):
                next_x, next_y = x + self.dx[delta], y + self.dy[delta]
                if (0 <= next_x < rows and 0 <= next_y < cols) and grid[next_x][next_y] == 1:
                    queue.append((next_x, next_y))

        return area
