class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if root is None:
            return node

        if root.val < node.val:
            root.right = self.insertNode(root.right, node)
        else:
            root.left = self.insertNode(root.left, node)

        return root
