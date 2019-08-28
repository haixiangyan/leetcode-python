class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <= 1:
            return n

        dp = [0 for i in range(n)]

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp)

        return dp[n - 1]
