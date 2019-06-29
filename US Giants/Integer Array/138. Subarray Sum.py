class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        if nums is None:
            return -1, -1

        prefix_hash = { 0: -1 }
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i

            prefix_hash[prefix_sum] = i

        return -1, -1
