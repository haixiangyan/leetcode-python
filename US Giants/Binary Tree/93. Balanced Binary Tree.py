class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        is_balance, _ = self.divide_conquer(root)
        return is_balance

    def divide_conquer(self, root):
        if root is None:
            return True, 0

        left_is_balance, left_depth = self.divide_conquer(root.left)
        right_is_balance, right_depth = self.divide_conquer(root.right)

        is_balance = left_is_balance and right_is_balance
        if is_balance:
            is_balance = abs(left_depth - right_depth) <= 1

        return is_balance, 1 + max(left_depth, right_depth)
