class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        if root is None:
            return root

        return self.dfs(root)

    def dfs(self, root):
        if root.left is None:
            return root

        newRoot = self.dfs(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None

        return newRoot
