class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    inorder_results = []

    def removeNode(self, root, value):
        # 获取中序遍历结果
        self.inorder(root, value)
        # 用中序遍历结果重新构造树
        new_root = self.build_tree(0, len(self.inorder_results) - 1)

        return new_root

    def inorder(self, root, value):
        if root is None:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.inorder_results.append(root.val)
        self.inorder(root.right, value)

    def build_tree(self, left, right):
        if left == right:
            return TreeNode(self.inorder_results[left])

        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(self.inorder_results[mid])
        node.left = self.build_tree(left, mid - 1)
        node.right = self.build_tree(mid + 1, right)

        return node
