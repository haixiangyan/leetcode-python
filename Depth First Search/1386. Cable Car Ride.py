class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, -1, 1, -1]
        self.dy = [1, 0, -1, 0, 1, 1, -1, -1]

    def cableCarRide(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        memo = [[-1 for _ in range(cols)] for _ in range(rows)]

        cost = 0

        for i in range(rows):
            for j in range(cols):
                cost = max(cost, self.dfs(matrix, i, j, rows, cols, memo))

        return cost

    def dfs(self, matrix, x, y, rows, cols, memo):
        if memo[x][y] != -1:
            return memo[x][y]

        cost = 1

        for delta in range(8):
            next_x, next_y = x + self.dx[delta], y + self.dy[delta]
            if 0 <= next_x < rows and 0 <= next_y < cols and matrix[next_x][next_y] > matrix[x][y]:
                cost = max(cost, self.dfs(matrix, next_x, next_y, rows, cols, memo) + 1)

        memo[x][y] = cost

        return cost
