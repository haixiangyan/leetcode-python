import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        prefix_sums = [(0, -1)]

        for i, num in enumerate(nums):
            prefix_sums.append(
                (prefix_sums[-1][0] + num, i)
            )

        prefix_sums.sort()

        closest = sys.maxsize
        result = [-1, -1]

        for i in range(1, len(prefix_sums)):
            if prefix_sums[i][0] - prefix_sums[i - 1][0] < closest:
                # Update closest sum
                closest = prefix_sums[i][0] - prefix_sums[i - 1][0]

                # Update first index and last index
                result = [
                    min(prefix_sums[i][1], prefix_sums[i - 1][1]) + 1,
                    max(prefix_sums[i][1], prefix_sums[i - 1][1])
                ]

        return result
