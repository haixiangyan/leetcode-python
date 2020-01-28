class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        if not nums:
            return 0

        n = len(nums)
        for i in range(n):
            while 0 <= nums[i] < n and i != nums[i]:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp

        for i in range(n):
            if i != nums[i]:
                return i
        return n
