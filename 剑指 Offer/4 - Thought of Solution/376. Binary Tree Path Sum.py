class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        result = []
        path = []

        self.dfs(root, result, path, 0, target)

        return result

    def dfs(self, root, result, path, curtSum, target):
        if root is None:
            return

        path.append(root.val)
        curtSum += root.val

        if root.left is None and root.right is None and curtSum == target:
            result.append(path[:])

        self.dfs(root.left, result, path, curtSum, target)
        self.dfs(root.right, result, path, curtSum, target)

        path.pop()
