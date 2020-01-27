class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root is None:
            return root

        self.divide_conquer(root)

        return root

    def divide_conquer(self, root):
        if root is None:
            return None

        left_tail = self.divide_conquer(root.left)
        right_tail = self.divide_conquer(root.right)

        if left_tail is not None:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail or left_tail or root
