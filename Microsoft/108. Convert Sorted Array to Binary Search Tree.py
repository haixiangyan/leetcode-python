class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.divide_conquer(nums, 0, len(nums) - 1)

    def divide_conquer(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.divide_conquer(nums, left, mid - 1)
        root.right = self.divide_conquer(nums, mid + 1, right)

        return root
