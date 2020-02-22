class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if root is None:
            return ['#']
        order = [str(root.val)]
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return order + left + right

    def deserialize(self, data):
        char = data.pop(0)
        if char == '#':
            return None
        else:
            root = TreeNode(int(char))

        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
