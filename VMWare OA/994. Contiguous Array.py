class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        prefix_sum, table, longest = 0, {0:0}, 0

        for i, num in enumerate(nums):
            prefix_sum += num if num == 1 else -1

            if prefix_sum in table:
                longest = max(longest, i + 1 - table[prefix_sum])
            else:
                table[prefix_sum] = i + 1

        return longest
