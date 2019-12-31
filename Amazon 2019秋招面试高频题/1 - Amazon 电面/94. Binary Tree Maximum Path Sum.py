class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        max_sum, _ = self.divide_conquer(root)

        return max_sum

    def divide_conquer(self, root):
        if root is None:
            return float('-inf'), 0

        left_max_sum, left_single = self.divide_conquer(root.left)
        right_max_sum, right_single = self.divide_conquer(root.right)

        max_sum = max(left_max_sum, right_max_sum, left_single + root.val + right_single)
        single = max(left_single + root.val, right_single + root.val, 0)

        return max_sum, single