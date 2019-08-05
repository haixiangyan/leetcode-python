class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0

        return self.divide_conquer(root)

    def divide_conquer(self, root):
        if root is None:
            return 0

        left_min_depth = self.divide_conquer(root.left)
        right_min_depth = self.divide_conquer(root.right)

        if root.left is None:
            return right_min_depth + 1
        if root.right is None:
            return left_min_depth + 1

        return min(left_min_depth, right_min_depth) + 1
