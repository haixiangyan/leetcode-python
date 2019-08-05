class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n - 2)]

            for i in range(3, n + 1):
                # 左边节点数
                for j in range(1, i + 1):
                    dp[i] += dp[j - 1] * dp[i - j]

            return dp[n]
