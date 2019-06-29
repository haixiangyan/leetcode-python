class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return

        unique_length = 0

        for i in range(1, len(nums)):
            if nums[unique_length] != nums[i]:
                unique_length += 1
                nums[unique_length] = nums[i]

        return unique_length + 1
