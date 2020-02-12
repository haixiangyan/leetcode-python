class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        if len(A) == 0:
            return 0
        if len(A) <= 2:
            return max(A)

        n = len(A)
        dp = [0 for _ in range(n)]
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i])

        return dp[-1]
