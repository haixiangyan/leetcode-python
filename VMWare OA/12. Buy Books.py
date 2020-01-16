class Solution:
    def buy_books(self, sizes, costs, budget):
        n = len(sizes)

        dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, budget + 1):
                if costs[i - 1] > budget:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + sizes[i])

        return dp[-1][-1]
