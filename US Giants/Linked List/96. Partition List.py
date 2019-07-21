class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        left_dummy, right_dummy = ListNode(0), ListNode(0)
        left, right = left_dummy, right_dummy

        while head is not None:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            else:
                right.next = ListNode(head.val)
                right = right.next

            head = head.next

        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
