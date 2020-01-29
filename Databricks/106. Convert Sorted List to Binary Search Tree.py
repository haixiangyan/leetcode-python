class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        # Find middle
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        parent = TreeNode(middle.val)

        parent.left = self.sortedListToBST(head)
        parent.right = self.sortedListToBST(middle.next)

        return parent
