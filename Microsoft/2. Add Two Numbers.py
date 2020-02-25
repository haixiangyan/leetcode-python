class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        carry = 0

        while True:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            node.val = carry % 10
            carry = carry // 10

            if l1 or l2 or carry != 0:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        return head
