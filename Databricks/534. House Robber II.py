class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0], dp[1] = 0, nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        money = dp[n - 1]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(money, dp[n - 2])
