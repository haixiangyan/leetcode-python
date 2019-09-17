class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root:
    @return: the sum of leafnode
    """
    def sumLeafNode(self, root):
        if root.left is None and root.right is None:
            return root.val

        leftSum, rightSum = 0, 0
        if root.left is not None:
            leftSum = self.sumLeafNode(root.left)
        if root.right is not None:
            rightSum = self.sumLeafNode(root.right)

        return leftSum + rightSum
