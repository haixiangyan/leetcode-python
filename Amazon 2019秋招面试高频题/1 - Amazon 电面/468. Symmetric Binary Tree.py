class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        if root:
            return self.compare(root.left, root.right)
        return True

    def compare(self, left, right):
        if left is None and right is None:
            return True

        if left and right and left.val == right.val:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)

        return False
