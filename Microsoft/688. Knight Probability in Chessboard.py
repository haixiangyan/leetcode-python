class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        next = [[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
        for step in range(1, K + 1):
            dpTemp = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for dx, dy in next:
                        lastR, lastC = i - dx, j - dy
                        if 0 <= lastC < N and 0 <= lastR < N:
                            dpTemp[i][j] += dp[lastR][lastC] * .125

            dp = dpTemp

        result = 0.0
        for i in range(N):
            for j in range(N):
                result += dp[i][j]

        return result
