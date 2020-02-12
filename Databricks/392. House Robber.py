class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        if not A:
            return 0

        n = len(A)
        dp = [0 for _ in range(n + 1)]
        dp[1] = A[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])

        return dp[-1]
