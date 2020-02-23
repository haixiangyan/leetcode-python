class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        is_bst, _, _ = self.dfs(root)

        return is_bst

    def dfs(self, root):
        if root is None:
            return True, None, None

        left_is_bst, left_min, left_max = self.dfs(root.left)
        right_is_bst, right_min, right_max = self.dfs(root.right)

        if not left_is_bst or not right_is_bst:
            return False, None, None
        if left_max and left_max.val >= root.val:
            return False, None, None
        if right_min and right_min.val <= root.val:
            return False, None, None

        root_min = left_min or root
        root_max = right_max or root

        return True, root_min, root_max
