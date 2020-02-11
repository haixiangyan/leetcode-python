class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        max_len, _, _ = self.dfs(root)
        return max_len

    def dfs(self, root):
        if root is None:
            return 0, 0, 0

        max_len, up, down = 0, 0, 0
        for child in root.children:
            child_max_len, child_up, child_down = self.dfs(child)
            max_len = max(max_len, child_max_len)

            if child.val + 1 == root.val:
                down = max(down, child_down + 1)
            if child.val - 1 == root.val:
                up = max(up, child_up + 1)

        max_len = max(max_len, up + 1 + down)

        return max_len, up, down
