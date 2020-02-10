class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.leaves = []
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        self.tree_height(root)

        return self.leaves

    def tree_height(self, root):
        if root is None:
            return -1

        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)

        height = max(left_height, right_height) + 1
        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)

        return height
