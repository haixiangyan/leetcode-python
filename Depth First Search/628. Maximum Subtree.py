class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
        self.max_subtree = None
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        if root is None:
            return None

        self.tree_sum(root)

        return self.max_subtree

    def tree_sum(self, root):
        if root is None:
            return 0

        left_sum = self.tree_sum(root.left)
        right_sum = self.tree_sum(root.right)

        curt_sum = left_sum + root.val + right_sum
        if curt_sum > self.max_sum:
            self.max_sum = curt_sum
            self.max_subtree = root

        return curt_sum
