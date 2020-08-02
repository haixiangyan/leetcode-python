from collections import deque


class Solution:
    DX = [1, 0, -1, 0]
    DY = [0, 1, 0, -1]

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1

        return count

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        grid[i][j] = '0'

        while queue:
            x, y = queue.popleft()

            for delta in range(4):
                next_x, next_y = x + self.DX[delta], y + self.DY[delta]

                if not self.isValid(grid, next_x, next_y):
                    continue

                queue.append((next_x, next_y))
                grid[next_x][next_y] = '0'

    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'
