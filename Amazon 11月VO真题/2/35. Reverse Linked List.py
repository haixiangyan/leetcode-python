class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if head is None or head.next is None:
            return head

        prev, curt = None, head
        while curt is not None:
            next = curt.next

            curt.next = prev
            prev = curt
            curt = next

        return prev
