from collections import deque

class Solution:
    def max_square(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    side = self.get_side(dp, i, j)
                    max_area = max(max_area, side * side)
                    dp[i][j] = side * side

        return max_area

    def get_side(self, dp, i, j):
        if i == 0 or j == 0:
            return 1

        left_square_side = dp[i - 1][j]
        top_square_side = dp[i][j - 1]
        top_left__square_side = dp[i - 1][j - 1]

        return min(left_square_side, top_square_side, top_left__square_side) + 1


s = Solution()
matrix = [
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1],
]
print(s.max_square(matrix))