class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, prev):
        if root is None:
            return 0

        curt = 10 * prev + root.val
        if not root.left and not root.right:
            return curt

        return self.dfs(root.left, curt) + self.dfs(root.right, curt)
