class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        if root is None:
            return 0

        left_sum = self.maxPathSum2(root.left)
        right_sum = self.maxPathSum2(root.right)

        return max(root.val, left_sum + root.val, right_sum + root.val)
