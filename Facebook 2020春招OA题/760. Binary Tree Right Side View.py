class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.view = []
        self.length = 0
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def rightSideView(self, root):
        if root is None:
            return []

        self.dfs(root, 0)

        return self.view

    def dfs(self, root, depth):
        if root is None:
            return

        if depth == self.length:
            self.view.append(root.val)
            self.length += 1

        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)
