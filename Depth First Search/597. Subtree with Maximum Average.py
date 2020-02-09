class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.max_avg = float('-inf')
        self.max_root = None
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        if root is None:
            return None

        self.dfs(root)

        return self.max_root

    def dfs(self, root):
        if root is None:
            return float('-inf'), 0

        left_total, left_num = self.dfs(root.left)
        right_total, right_num = self.dfs(root.right)

        total = root.val
        num = 1

        if left_num > 0:
            total += left_total
            num += left_num
        if right_num > 0:
            total += right_total
            num += right_num

        if total / num > self.max_avg:
            self.max_avg = total / num
            self.max_root = root

        return total, num
