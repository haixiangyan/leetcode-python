class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def findClosestLeaf(self, root, k):
        parents = {}
        node = self.dfs(root, parents, k)

        queue = [node]
        visited = {node}

        while queue:
            first = queue[0]

            if first.left is None and first.right is None:
                return first.val
            if first.left and first.left not in visited:
                queue.append(first.left)
                visited.add(first.left)
            if first.right and first.right not in visited:
                queue.append(first.right)
                visited.add(first.right)
            if first in parents and parents[first] not in visited:
                queue.append(parents[first])
                visited.add(parents[first])

            queue.pop(0)
        return 0

    def dfs(self, root, parents, k):
        result = root
        node = None

        if root.left:
            parents[root.left] = root
            node = self.dfs(root.left, parents, k)
            if node.val == k:
                result = node

        if root.right:
            parents[root.right] = root
            node = self.dfs(root.right, parents, k)
            if node.val == k:
                result = node

        return result
