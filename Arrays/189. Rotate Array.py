class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if (len(nums) <= 1):
            return

        length = len(nums)
        k = k % length

        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)
    

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        