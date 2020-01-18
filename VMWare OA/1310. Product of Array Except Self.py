class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        n = len(nums)
        products = [1 for _ in range(n)]

        leading = 1
        for i in range(n):
            products[i] = leading
            leading *= nums[i]

        trailing = 1
        for i in range(n - 1, -1, -1):
            products[i] *= trailing
            trailing *= nums[i]

        return products
