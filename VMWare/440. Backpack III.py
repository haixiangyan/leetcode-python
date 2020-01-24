class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII_1(self, A, V, m):
        n = len(A)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 先赋值，好作比较
                dp[i][j] = dp[i - 1][j]

                counts = 1
                while j >= counts * A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - counts * A[i - 1]] + counts * V[i - 1])
                    counts += 1

        return dp[-1][-1]

    def backPackIII_2(self, A, V, m):
        n = len(A)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 先赋值，好作比较
                dp[i][j] = dp[i - 1][j]

                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - A[i - 1]] + V[i - 1])

        return dp[-1][-1]
