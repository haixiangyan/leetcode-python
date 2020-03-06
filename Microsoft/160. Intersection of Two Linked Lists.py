class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = self.get_length(headA)
        l2 = self.get_length(headB)

        if l1 > l2:
            headA, headB = headB, headA
            l1, l2 = l2, l1

        offset = l2 - l1
        for _ in range(offset):
            headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
