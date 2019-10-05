class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        node = head
        for _ in range(n):
            node = node.next

        dummy = ListNode(0, head)
        prev = dummy
        while node is not None:
            node = node.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
