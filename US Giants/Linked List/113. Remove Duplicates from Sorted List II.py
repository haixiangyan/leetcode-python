class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        parent = dummy
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                duplicate_val = current.val

                while current is not None and current.val == duplicate_val:
                    current = current.next

                parent.next = current
            else:
                current = current.next
                parent = parent.next

        return dummy.next
