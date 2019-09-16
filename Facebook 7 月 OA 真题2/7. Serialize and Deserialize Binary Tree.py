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

        queue = deque([root])
        result = [root.val]

        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                node = queue.popleft()
                result.append(root.val if node else '#')

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

        return ','.join(result)

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

        nodeValues = data.split(',')
        root = TreeNode(nodeValues[0])
        queue = deque({"node": root, "index": 0})

        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                info = queue.popleft()

                leftNodeValue = nodeValues[2 * info.index + 1]
                rightNodeValue = nodeValues[2 * info.index + 2]

                info.node.left = None if leftNodeValue == '#' else TreeNode(leftNodeValue)
                info.node.right = None if rightNodeValue == '#' else TreeNode(rightNodeValue)

                queue.append({"node": info.node.left, "index": (2 * info.index + 1)})
                queue.append({"node": info.node.right, "index": (2 * info.index + 2)})

        return root
