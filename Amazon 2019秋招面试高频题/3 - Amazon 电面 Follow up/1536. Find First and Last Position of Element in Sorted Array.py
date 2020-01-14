class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        upper = self.find_upper(nums, target)
        lower = self.find_lower(nums, target)

        return [lower, upper]


    def find_upper(self, nums, target):
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

    def find_lower(self, nums, target):
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
