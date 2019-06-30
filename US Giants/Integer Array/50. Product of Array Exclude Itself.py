class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        if nums is None:
            return []

        length = len(nums)

        B = [0 for i in range(length)]

        suffix_products = [0 for i in range(length + 1)]
        suffix_products[length] = 1

        # Compute suffix products
        for i in range(length - 1, 0, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i]

        prefix_product = 1
        for i in range(length):
            B[i] = prefix_product * suffix_products[i + 1]
            prefix_product *= nums[i]

        return B
