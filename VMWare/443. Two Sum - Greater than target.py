class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        counts = 0
        while left < right:
            curt_sum = nums[left] + nums[right]
            if curt_sum > target:
                counts += right - left
                right -= 1
            else:
                left += 1

        return counts
