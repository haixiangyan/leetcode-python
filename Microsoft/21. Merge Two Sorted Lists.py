class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curt = dummy

        while l1 or l2:
            if not l2 or (l1 and l1.val < l2.val):
                curt.next = l1
                l1 = l1.next
            else:
                curt.next = l2
                l2 = l2.next
            curt = curt.next

        return dummy.next
