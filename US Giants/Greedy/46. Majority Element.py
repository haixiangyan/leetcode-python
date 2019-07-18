class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        current_major = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                current_major = nums[i]

            if nums[i] == current_major:
                count += 1
            else:
                count -= 1

        return current_major
