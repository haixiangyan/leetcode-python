from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        index_to_node = {}
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            if node:
                queue.append((node.left, index - 1))
                queue.append((node.right, index + 1))
                if index not in index_to_node:
                    index_to_node[index] = []
                index_to_node[index].append(node.val)

        return [index_to_node[index] for index in sorted(index_to_node)]
