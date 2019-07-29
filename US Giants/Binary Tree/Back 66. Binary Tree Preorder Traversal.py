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

        self.pre_order(root, results)

        return results

    def pre_order(self, root, results):
        if root is None:
            return

        results.append(root.val)

        self.pre_order(root.left, results)
        self.pre_order(root.right, results)
