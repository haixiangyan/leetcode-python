class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if root is None:
            return None

        result = TreeNode(root.val)
        if root.children:
            result.left = self.encode(root.children[0])

        curt = result.left

        for i in range(1, len(root.children)):
            curt.right = self.encode(root.children[i])
            curt = curt.right

        return result

    # Decodes your binary tree to an n-ary tree.
    def decode(self, root: TreeNode) -> 'Node':
        if root is None:
            return None

        result = Node(root.val, [])
        curt = root.left

        while curt:
            result.children.append(self.decode(curt))
            curt = curt.right
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))