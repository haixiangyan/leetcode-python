class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        if root is None:
            return 0

        return self.divide_conquer(root, None, 0)

    def divide_conquer(self, root, parent, length):
        if root is None:
            return length

        # 临时长度
        if parent and parent.val + 1 == root.val:
            length += 1
        else:
            length = 1

        left = self.divide_conquer(root.left, root, length)
        right = self.divide_conquer(root.right, root, length)

        return max(left, right, length)
