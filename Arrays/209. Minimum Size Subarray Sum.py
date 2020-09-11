class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        j, n, curt_sum = 0, len(nums), 0
        min_len = n + 1

        for i in range(n):
            while j < n and curt_sum < s:
                curt_sum += nums[j]
                j += 1
            
            if curt_sum >= s:
                min_len = min(min_len, j - i)
            
            curt_sum -= nums[i]
        
        return 0 if min_len == n + 1 else min_len
