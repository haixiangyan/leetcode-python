class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        if not root:
            return True

        is_valid, _, _ = self.dfs(root)

        return is_valid

    def dfs(self, root):
        if root is None:
            return True, None, None

        left_valid, left_min, left_max = self.dfs(root.left)
        right_valid, right_min, right_max = self.dfs(root.right)

        if not left_valid or not right_valid:
            return False, None, None
        if left_max and left_max.val >= root.val:
            return False, None, None
        if right_min and right_min.val <= root.val:
            return False, None, None

        curt_min = left_min if left_min else root
        curt_max = right_max if right_max else root

        return True, curt_min, curt_max
