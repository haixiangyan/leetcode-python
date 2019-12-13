class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        if not nums or n < 1 or n > len(nums):
            return -1
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - n)

    def quickselect(self, nums, start, end, k):
        if start == end:
            return nums[k]
        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quickselect(nums, start, right, k)
        if k >= left:
            return self.quickselect(nums, left, end, k)

        return nums[k]
