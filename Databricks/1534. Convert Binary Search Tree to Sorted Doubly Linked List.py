class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.prev = None
        self.first = None

    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if root is None:
            return root

        self.inorder(root)

        self.first.left = self.prev
        self.prev.right = self.first

        return self.first

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if self.first is None:
            self.first = root

        if self.prev is not None:
            self.prev.right = root
            root.left = self.prev
        self.prev = root

        self.inorder(root.right)
