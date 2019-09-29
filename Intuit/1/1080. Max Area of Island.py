from collections import deque
class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.bfs(grid, i, j))

        return maxArea

    def bfs(self, grid, x, y):
        count = 1
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(x, y)])
        grid[x][y] = 0

        while queue:
            curX, curY = queue.popleft()
            for dx, dy in direction:
                nextX, nextY = curX + dx, curY + dy

                if not self.isValid(grid, nextX, nextY):
                    continue
                queue.append((nextX, nextY))
                grid[nextX][nextY] = 0
                count += 1

        return count

    def isValid(self, grid, x, y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1
