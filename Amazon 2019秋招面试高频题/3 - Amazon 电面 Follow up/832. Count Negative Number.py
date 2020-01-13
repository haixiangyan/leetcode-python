class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        if not nums or not nums[0]:
            return 0

        counts = 0

        end = len(nums[0]) - 1
        for row in nums:
            while end >= 0:
                if row[end] < 0:
                    break
                end -= 1
            counts += end + 1

        return counts
