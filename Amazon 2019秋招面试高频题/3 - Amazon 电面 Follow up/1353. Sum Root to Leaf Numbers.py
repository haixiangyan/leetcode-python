class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        if root is None:
            return 0

        return self.dfs(root, 0)

    def dfs(self, root, prev):
        if root is None:
            return 0

        curt_sum = root.val + prev * 10

        if root.left is None and root.right is None:
            return curt_sum

        return self.dfs(root.left, curt_sum) + self.dfs(root.right, curt_sum)
