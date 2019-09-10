class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0

        dp = [1] * len(nums)

        for current, value in enumerate(nums):
            for i in range(current):
                if nums[i] < value:
                    dp[current] = max(dp[current], dp[i] + 1)

        return max(dp)
