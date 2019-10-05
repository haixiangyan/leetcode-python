class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if not nums:
            return nums

        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 != 0:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
