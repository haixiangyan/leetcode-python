class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """
    def isSymmetric(self, root):
        if not root:
            return True

        return self.divideConquer(root.left, root.right)

    def divideConquer(self, left, right):
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        return self.divideConquer(left.right, right.left) and self.divideConquer(left.left, right.right)
