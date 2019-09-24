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

        back = None
        while head is not None:
            temp = head.next
            head.next = back
            back = head
            head = temp

        return back
