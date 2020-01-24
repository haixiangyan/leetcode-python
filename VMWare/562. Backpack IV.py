class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for num in nums:
            for i in range(num, target + 1):
                dp[i] += dp[i - num]

        return dp[target]
