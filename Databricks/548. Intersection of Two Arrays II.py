import collections


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        store = collections.Counter(nums1)
        results = []

        for num in nums2:
            if store[num] > 0:
                results.append(num)
                store[num] -= 1

        return results
