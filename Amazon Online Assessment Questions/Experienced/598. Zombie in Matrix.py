from collections import deque

class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # Initialize all zombies
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
        days = 0

        while queue:
            # Day += 1
            days += 1

            for _ in range(len(queue)):
                # Pop each
                x, y = queue.popleft()

                # Find neighbors
                for delta in range(4):
                    next_x, next_y = x + self.dx[delta], y + self.dy[delta]
                    # Turn to zombies
                    if self.is_valid(grid, next_x, next_y):
                        grid[next_x][next_y] = 1
                        queue.append((next_x, next_y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1

        return days - 1

    def is_valid(self, grid, x, y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0