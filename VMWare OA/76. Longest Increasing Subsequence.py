class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
