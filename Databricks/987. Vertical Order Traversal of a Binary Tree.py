from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode):
        if root is None:
            return []

        mapping = []

        self.dfs(root, mapping, 0, 0)

        store = defaultdict(list)
        mapping = sorted(mapping, key=lambda x: (x[0], x[1], x[2]))

        for item in mapping:
            store[item[0]].append(item[2])

        return store.values()

    def dfs(self, root, mapping, x, y):
        if root:
            mapping.append((x, y, root.val))
            self.dfs(root.left, mapping, x - 1, y + 1)
            self.dfs(root.right, mapping, x + 1, y + 1)
