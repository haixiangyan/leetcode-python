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
        if not root:
            return ''

        order = []
        queue = deque([root])
        while queue:
            queueLength = len(queue)
            for _ in range(queueLength):
                node = queue.popleft()
                order.append(str(node.val) if node else '#')

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        return ','.join(order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if not data or data == '':
            return None

        order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split(',')
        ]

        root = order[0]
        nodes = [root]
        slowIndex, fastIndex = 0, 1

        while slowIndex < len(nodes):
            node = nodes[slowIndex]
            node.left = order[fastIndex]
            node.right = order[fastIndex + 1]

            slowIndex += 1
            fastIndex += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root
