class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        result = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummy.next = ListNode(l2.val)
                l2 = l2.next

            dummy = dummy.next

        while l1 is not None:
            dummy.next = ListNode(l1.val)

            dummy = dummy.next
            l1 = l1.next

        while l2 is not None:
            dummy.next = ListNode(l2.val)

            dummy = dummy.next
            l2 = l2.next

        return result.next
