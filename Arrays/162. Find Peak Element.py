from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid
        
        if nums[left] < nums[right]:
            return right
        else:
            return left
