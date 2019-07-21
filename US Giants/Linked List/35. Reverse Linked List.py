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
        prev_node = None

        while head is not None:
            next_node = head.next

            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node
