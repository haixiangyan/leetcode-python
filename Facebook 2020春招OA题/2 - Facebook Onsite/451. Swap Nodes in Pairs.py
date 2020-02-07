class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        if head is None:
            return

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = head

        while first is not None and first.next is not None:
            second = first.next

            temp = second.next

            prev.next = second
            second.next = first
            first.next = temp

            prev = first
            first = temp

        return dummy.next
