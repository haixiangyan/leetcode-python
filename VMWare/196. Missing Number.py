class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        if not nums:
            return 0

        i, n = 0, len(nums)
        while i < n:
            while nums[i] != i and nums[i] < n:
                next_num = nums[i]
                nums[i] = nums[next_num]
                nums[next_num] = next_num
            i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n
