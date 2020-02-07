class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        nums1, nums2 = sorted(nums1), sorted(nums2)

        results = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not results or results[-1] != nums1[i]:
                    results.append(nums1[i])
                i += 1
                j += 1
        return results
