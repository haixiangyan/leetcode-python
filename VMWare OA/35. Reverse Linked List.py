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
        prev = None
        node = head

        while node is not None:
            temp = node.next

            node.next = prev

            prev = node
            node = temp

        return prev
