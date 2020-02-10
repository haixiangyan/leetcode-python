class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.min_subtree = None
        self.min_sum = float('inf')
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        if root is None:
            return None

        self.divide_conquer(root)

        return self.min_subtree

    def divide_conquer(self, root):
        if root is None:
            return 0

        left_sum = self.divide_conquer(root.left)
        right_sum = self.divide_conquer(root.right)

        curt_sum = left_sum + right_sum + root.val
        if curt_sum < self.min_sum:
            self.min_sum = curt_sum
            self.min_subtree = root

        return curt_sum
