class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.diameter = 0
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        self.divide_conquer(root)

        return self.diameter

    def divide_conquer(self, root):
        if root is None:
            return 0

        left = self.divide_conquer(root.left)
        right = self.divide_conquer(root.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)
