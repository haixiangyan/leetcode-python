class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        self.dfs(root)

        return self.diameter

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1
