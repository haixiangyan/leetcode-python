class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []

        results = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)

        while i < n1 and j < n2:
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
