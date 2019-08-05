class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        results = []

        self.preorder(root, results)

        return results

    def preorder(self, root, results):
        if root is None:
            return

        results.append(root.val)
        self.preorder(root.left, results)
        self.preorder(root.right, results)
