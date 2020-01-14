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
    def binaryTreePathSum2(self, root, target):
        paths = []

        if root is None:
            return paths

        self.dfs(root, 0, target, paths, [])

        return paths

    def dfs(self, root, end, target, paths, path):
        if root is None:
            return

        path.append(root.val)

        temp = target
        for i in range(end, -1, -1):
            temp = temp - path[i]
            if temp == 0:
                paths.append(path[i:])

        self.dfs(root.left, end + 1, target, paths, path)
        self.dfs(root.right, end + 1, target, paths, path)

        path.pop()
