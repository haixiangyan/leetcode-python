from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        if target > nums[right]:
            return right + 1
        if target == nums[right]:
            return right
        if target > nums[left]:
            return left + 1

        return left