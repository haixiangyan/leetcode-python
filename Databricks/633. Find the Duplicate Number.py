class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        if not nums:
            return 0

        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return nums[i]
        return 0
