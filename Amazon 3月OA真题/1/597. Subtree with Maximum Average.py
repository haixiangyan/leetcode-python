class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.maxAvg = float('-inf')
        self.subtree = None
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        if root is None:
            return None

        self.helper(root)

        return self.subtree

    def helper(self, root):
        if root is None:
            return 0, 0

        leftSum, leftNum = 0, 0
        rightSum, rightNum = 0, 0
        if root.left:
            leftSum, leftNum = self.helper(root.left)
        if root.right:
            rightSum, rightNum = self.helper(root.right)

        currentSum, currentNum = leftSum + rightSum + root.val, leftNum + rightNum + 1
        currentAvg = currentSum / currentNum

        if currentAvg > self.maxAvg:
            self.maxAvg = currentAvg
            self.subtree = root

        return currentSum, currentNum
