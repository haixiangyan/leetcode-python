class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0

        left = self.rangeSumBST(root.left, L, R)
        right = self.rangeSumBST(root.right, L, R)

        return left + right + (root.val if L <= root.val <= R else 0)
