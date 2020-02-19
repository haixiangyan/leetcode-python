class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]

        trees = []
        for root_val in range(start, end + 1):
            left_subtrees = self.dfs(start, root_val - 1)
            right_subtrees = self.dfs(root_val + 1, end)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(root_val)
                    root.left = left_subtree
                    root.right = right_subtree

                    trees.append(root)
        return trees
