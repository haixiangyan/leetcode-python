class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        max_sum, _ = self.dfs(root)

        return max_sum

    def dfs(self, root):
        if root is None:
            return float('-inf'), 0

        left_max_sum, left_single = self.dfs(root.left)
        right_max_sum, right_single = self.dfs(root.right)

        max_sum = max(left_max_sum, right_max_sum, left_single + root.val + right_single)
        single = max(left_single + root.val, right_single + root.val, 0)

        return max_sum, single
