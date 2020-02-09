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

        self.dfs(root, target, [], paths)

        return paths

    def dfs(self, root, target, path, paths):
        if root is None:
            return

        path.append(root.val)

        temp = target
        for i in range(len(path) - 1, -1, -1):
            temp -= path[i]
            if temp == 0:
                paths.append(path[i:])

        self.dfs(root.left, target, path, paths)
        self.dfs(root.right, target, path, paths)
        path.pop()
