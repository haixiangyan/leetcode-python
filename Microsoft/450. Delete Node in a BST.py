class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 只有一个 child 的情况
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 有两个 children 的情况，找到右节点的最左节点
            prev, next = root, root.right
            while next.left:
                prev = next
                next = next.left

            root.val = next.val
            # 如果有右节点的左节点
            if prev != root:
                prev.left = next.right
            else:
                prev.right = next.right
        return root
