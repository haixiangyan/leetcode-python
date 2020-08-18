from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1, -1]

        first_pos = self.find_first(nums, target)
        last_pos = self.find_last(nums, target)

        return [first_pos, last_pos]

    def find_first(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def find_last(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
