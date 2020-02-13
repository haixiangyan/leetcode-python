class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self):
        self.first = None
        self.prev = None

    """
    @param root: The root of tree
    @return: the head of doubly list node
    """

    def bstToDoublyList(self, root):
        if root is None:
            return root

        head, _ = self.dfs(root)

        return head

    def dfs(self, root):
        if root is None:
            return None, None

        left_head, left_tail = self.dfs(root.left)
        right_head, right_tail = self.dfs(root.right)

        curt = DoublyListNode(root.val)

        if left_tail:
            left_tail.next = curt
            curt.prev = left_tail
        if right_head:
            curt.next = right_head
            right_head.prev = curt

        head = left_head or curt or right_head
        tail = right_tail or curt or left_tail

        return head, tail
