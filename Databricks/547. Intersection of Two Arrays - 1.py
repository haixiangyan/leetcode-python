class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []

        n1, n2 = len(nums1), len(nums2)

        nums1 = sorted(nums1)
        common = set()

        for i in range(n2):
            if nums2[i] in common:
                continue
            if self.binary_search(nums1, n1, nums2[i]):
                common.add(nums2[i])

        return list(common)

    def binary_search(self, nums, n, target):
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return True

        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        return False
