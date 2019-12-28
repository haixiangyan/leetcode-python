class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy

        # Merge two lists with same minimum length
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next

            node = node.next

        # Try to merge l1
        while l1 is not None:
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next

        # Try to merge l2
        while l2 is not None:
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next

        # Return result
        return dummy.next