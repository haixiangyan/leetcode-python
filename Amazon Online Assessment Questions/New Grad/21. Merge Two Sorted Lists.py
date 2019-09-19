class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        head = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        while l1 is not None:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2 is not None:
            head.next = l2
            l2= l2.next
            head = head.next

        return dummy.next
