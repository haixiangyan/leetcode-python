class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def reachEndpoint(self, map):
        if not map or not map[0]:
            return True

        rows, cols = len(map), len(map[0])

        return self.dfs(map, 0, 0, rows, cols, set())

    def dfs(self, map, x, y, rows, cols, visited):
        if not (0 <= x < rows and 0 <= y < cols) or map[x][y] == 0:
            return False

        if map[x][y] == 9:
            return True

        visited.add((x, y))

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]

            if (next_x, next_y) in visited:
                continue

            reach = self.dfs(map, next_x, next_y, rows, cols, visited)

            if reach:
                return True

        return False
