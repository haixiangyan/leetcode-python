class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0

        prefix_sum = 0
        min_sum, max_sum = float('inf'), float('-inf')

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
