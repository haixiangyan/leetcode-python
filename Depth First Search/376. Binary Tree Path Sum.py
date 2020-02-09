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
        paths = []

        self.dfs(root, 0, target, [], paths)

        return paths

    def dfs(self, root, curt_sum, target, path, paths):
        if root is None:
            return

        path.append(root.val)
        curt_sum += root.val

        if not root.left and not root.right and curt_sum == target:
            paths.append(path[:])
            path.pop()
            return

        self.dfs(root.left, curt_sum, target, path, paths)
        self.dfs(root.right, curt_sum, target, path, paths)

        path.pop()
