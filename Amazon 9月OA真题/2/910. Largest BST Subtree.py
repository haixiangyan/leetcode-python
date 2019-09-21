class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class SubTree:
    def __init__(self, largest, n, minValue, maxValue):
        self.largest = largest
        self.n = n
        self.minValue = minValue
        self.maxValue = maxValue

class Solution:
    """
    @param root: the root
    @return: the largest subtree's size which is a Binary Search Tree
    """
    def largestBSTSubtree(self, root):
        if not root:
            return 0

        result = self.dfs(root)

        return result.largest

    def dfs(self, root):
        if root is None:
            return SubTree(0, 0, float('inf'), float('-inf'))

        leftResult = self.dfs(root.left)
        rightResult = self.dfs(root.right)

        if leftResult.maxValue < root.val < rightResult.minValue:
            n = leftResult.n + rightResult.n + 1
        else:
            n = float('-inf')

        largest = max(leftResult.largest, rightResult.largest, n)

        return SubTree(largest, n, min(leftResult.minValue, root.val), max(rightResult.maxValue, root.val))
