from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        if root is None:
            return []

        parents = {}
        self.find_parents(root, parents)

        queue = deque([target])
        visited = {target}

        distance = 0
        while queue and distance < K:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parents and parents[node] not in visited:
                    queue.append(parents[node])
                    visited.add(parents[node])
            distance += 1

        return [node.val for node in queue]

    def find_parents(self, root, parents):
        if root is None:
            return

        if root.left:
            parents[root.left] = root
            self.find_parents(root.left, parents)
        if root.right:
            parents[root.right] = root
            self.find_parents(root.right, parents)
