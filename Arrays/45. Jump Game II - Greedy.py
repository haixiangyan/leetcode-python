from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n, right_most, end = len(nums), 0, 0
        step = 0

        for i in range(n - 1):
            right_most = max(right_most, i + nums[i])

            if i == end:
                end = right_most
                step += 1
        
        return step
