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

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        while l1 is not None:
            node.next = l1
            l1 = l1.next
            node = node.next
        while l2 is not None:
            node.next = l2
            l2 = l2.next
            node = node.next

        return dummy.next
