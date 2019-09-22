class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.maxSubtree = None
        self.maxSum = float('-inf')
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        if root is None:
            return None

        self.dfs(root)

        return self.maxSubtree

    def dfs(self, root):
        if root is None:
            return 0

        leftSum = self.dfs(root.left)
        rightSum= self.dfs(root.right)

        curtMaxSum = leftSum + rightSum + root.val

        if curtMaxSum > self.maxSum:
            self.maxSum = curtMaxSum
            self.maxSubtree = root

        return leftSum + rightSum + root.val
