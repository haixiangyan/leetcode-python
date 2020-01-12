class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        islands = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    island = set()
                    self.dfs(grid, i, j, i, j, island)
                    islands.add(tuple(island))

        return len(islands)

    def dfs(self, grid, x, y, ox, oy, island):
        grid[x][y] = 0
        island.add((x - ox, y - oy))

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]
            if self.is_valid(grid, next_x, next_y):
                self.dfs(grid, next_x, next_y, ox, oy, island)

    def is_valid(self, grid, next_x, next_y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == 1
