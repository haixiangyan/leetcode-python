from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
                    
        return dp[-1]
