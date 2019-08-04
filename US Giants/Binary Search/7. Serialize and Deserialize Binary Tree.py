from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return ''

        queue = deque([root])
        results = []

        while len(queue) != 0:
            node = queue.popleft()

            results.append(str(node.val) if node is not None else '#')

            if node is not None:
                queue.append(node.left)
                queue.append(node.right)

        return ' '.join(results)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if not data:
            return None

        tree_nodes = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split(' ')
        ]

        root = tree_nodes[0]
        slow_index, fast_index = 0, 1
        nodes = [root]

        while slow_index < len(nodes):
            node = nodes[slow_index]

            node.left = tree_nodes[fast_index]
            node.right = tree_nodes[fast_index + 1]

            slow_index += 1
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root
