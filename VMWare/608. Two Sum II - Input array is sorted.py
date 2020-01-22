class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left < right:
            curt_sum = nums[left] + nums[right]

            if curt_sum < target:
                left += 1
            elif curt_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]
