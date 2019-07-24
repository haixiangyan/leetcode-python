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
        result = self.divide_conquer(head)
        return result

    def divide_conquer(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        mid = self.go_to_mid(head)

        right_head = mid.next
        mid.next = None

        root = TreeNode(right_head.val)
        root.left = self.divide_conquer(head)
        root.right = self.divide_conquer(right_head.next)

        return root

    def go_to_mid(self, head):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
