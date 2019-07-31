class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        if root is None:
            return []

        results = []

        self.findRange(root, k1, k2, results)

        return results

    def findRange(self, root, k1, k2, results):
        if root is None:
            return

        if k1 <= root.val <= k2:
            results.append(root.val)

        self.findRange(root.left, k1, k2, results)
        self.findRange(root.right, k1, k2, results)
