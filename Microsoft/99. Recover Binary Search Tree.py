class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.first, self.second = None, None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        self.inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if not self.first and self.prev.val > root.val:
            self.first = self.prev
        if self.first and self.prev.val > root.val:
            self.second = root

        self.prev = root

        self.inorder(root.right)
