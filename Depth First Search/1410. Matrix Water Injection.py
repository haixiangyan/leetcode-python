class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def waterInjection(self, matrix, R, C):
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        return 'YES' if self.dfs(matrix, R, C, rows, cols) else 'NO'

    def dfs(self, matrix, x, y, rows, cols):
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            return True

        for delta in range(4):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]
            if matrix[next_x][next_y] < matrix[x][y]:
                ok = self.dfs(matrix, next_x, next_y, rows, cols)
                if ok:
                    return True

        return False
