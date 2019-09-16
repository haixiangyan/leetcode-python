class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self):
        self.result = []

    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        if not root:
            return []

        self.dfs(root, target, 0, [])

        return self.result

    def dfs(self, root, target, length, path):
        if not root:
            return

        path.append(root.val)
        currentTarget = target

        # Check path
        for index in range(length, -1, -1):
            currentTarget -= path[index]
            if currentTarget == 0:
                self.result.append(path[index:])

        self.dfs(root.left, target, length + 1, path)
        self.dfs(root.right, target, length + 1, path)

        path.pop()
