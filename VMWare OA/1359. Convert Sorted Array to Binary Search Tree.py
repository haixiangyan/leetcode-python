class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param nums: the sorted array
    @return: the root of the tree
    """
    def convertSortedArraytoBinarySearchTree(self, nums):
        return self.divide_conquer(nums, 0, len(nums) - 1)

    def divide_conquer(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.divide_conquer(nums, start, mid - 1)
        root.right = self.divide_conquer(nums, mid + 1, end)

        return root
