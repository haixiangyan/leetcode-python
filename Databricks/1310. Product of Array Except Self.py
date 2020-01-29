class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        if not nums:
            return []

        n = len(nums)
        products = [1 for _ in range(n)]

        leading = 1
        for i in range(n):
            products[i] *= leading
            leading *= nums[i]

        tailing = 1
        for i in range(n - 1, -1, -1):
            products[i] *= tailing
            tailing *= nums[i]

        return products
