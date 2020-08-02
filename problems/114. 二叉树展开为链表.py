# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return None

        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)

        if not left_max:
            return right_max or root

        left_max.right = root.right
        root.right = root.left
        root.left = None

        return right_max or left_max or root
