# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)

        return left or root
