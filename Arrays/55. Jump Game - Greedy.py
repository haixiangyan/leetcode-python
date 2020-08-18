from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n, right_most = len(nums), 0

        for i in range(n):
            if right_most >= i:
                right_most = max(right_most, nums[i] + i)
                if right_most >= n - 1:
                    return True

        return False
