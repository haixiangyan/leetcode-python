"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        results = []

        self.inorder(root, results)

        return results

    def inorder(self, root, results):
        if root is None:
            return

        self.inorder(root.left, results)
        results.append(root.val)
        self.inorder(root.right, results)
