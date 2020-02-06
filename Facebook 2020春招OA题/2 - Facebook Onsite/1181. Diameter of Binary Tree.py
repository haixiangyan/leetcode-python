class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.result = 0
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        self.divide_conquer(root)
        return self.result

    def divide_conquer(self, root):
        if root is None:
            return 0

        left = self.divide_conquer(root.left)
        right = self.divide_conquer(root.right)

        self.result = max(self.result, left + right)
        return max(left, right) + 1
