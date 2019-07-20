class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

    def majorityNumber(self, nums, k):
        counts = {}
        max_count = 0
        majority = 0

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max_count:
                max_count = counts[num]
                majority = num

        return majority
