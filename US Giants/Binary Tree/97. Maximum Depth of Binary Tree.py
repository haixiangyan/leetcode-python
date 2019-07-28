class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if root is None:
            return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        return 1 + max(left_max, right_max)
