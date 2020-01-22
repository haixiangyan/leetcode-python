class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, target):
        paths = []

        self.dfs(root, [], target, paths)

        return paths

    def dfs(self, root, path, target, paths):
        if not root:
            return

        curt_path = path + [root.val]

        if root.left is None and root.right is None:
            if target - root.val == 0:
                paths.append(curt_path)
            return

        if root.left:
            self.dfs(root.left, curt_path, target - root.val, paths)
        if root.right:
            self.dfs(root.right, curt_path, target - root.val, paths)
