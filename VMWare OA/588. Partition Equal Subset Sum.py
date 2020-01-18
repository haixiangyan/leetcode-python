class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        if not nums:
            return False

        target = sum(nums)

        if target % 2 == 1:
            return False

        n, m = len(nums), target // 2
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

        return dp[-1][-1]
