from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def serialize(self, root):
        def dfs(root):
            if root is None:
                return ['#']
            return [str(root.val)] + dfs(root.left) + dfs(root.right)

        return ','.join(dfs(root))

    def deserialize(self, data):
        def dfs(data):
            if not data:
                return None
            if data[0] == '#':
                data.popleft()
                return None

            root = TreeNode(int(data.popleft()))
            root.left = dfs(data)
            root.right = dfs(data)

            return root

        if data == '#':
            return None

        data = deque(data.split(','))
        return dfs(data)
