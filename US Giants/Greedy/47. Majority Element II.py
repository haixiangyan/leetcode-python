class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        count_table = {}

        for i, num in enumerate(nums):
            if num in count_table:
                count_table[num] += 1
            else:
                count_table[num] = 1

        length = len(nums)

        for key in count_table:
            if count_table[key] > length // 3:
                return key

        return None
