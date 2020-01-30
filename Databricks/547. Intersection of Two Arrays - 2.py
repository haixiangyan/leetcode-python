class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []

        set1, results = set(nums1), set()

        for num in nums2:
            if num in set1 and num not in results:
                results.add(num)

        return list(results)
