class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """

    def findSecondMinimumValue(self, root):
        self.root = root
        self.limit = float('inf')

        self.dfs(root)

        return -1 if self.limit == float('inf') else self.limit


    def dfs(self, node):
        if not node:
            return
        if self.root.val < node.val < self.limit:
            self.limit = node.val

        self.dfs(node.left)
        self.dfs(node.right)
