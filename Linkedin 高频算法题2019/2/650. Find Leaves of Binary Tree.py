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
        self.treeHeight(root)
        return self.leaves

    def treeHeight(self, root):
        if root is None:
            return -1

        leftHeight = self.treeHeight(root.left)
        rightHeight = self.treeHeight(root.right)
        height = 1 + max(leftHeight, rightHeight)

        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)
        return height

