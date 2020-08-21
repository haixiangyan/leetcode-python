from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        for i in range(len(nums)):
            if nums[i] == target:
                return True

        return False
