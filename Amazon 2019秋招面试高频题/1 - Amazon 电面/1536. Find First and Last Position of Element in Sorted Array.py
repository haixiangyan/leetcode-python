class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        lowerbound = self.find_lowerbound(nums, target)
        upperbound = self.find_upperbound(nums, target)

        return [lowerbound, upperbound]

    def find_lowerbound(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1

    def find_upperbound(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left

        return -1